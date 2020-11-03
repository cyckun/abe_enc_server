# -*- coding: utf-8 -*-
"""
    :author: Cao YongChao
    :mail: cyckun@aliyun.com
    :copyright: © 2020 Cao YongChao
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function
import pyopenabe
from xmlrpc.server import SimpleXMLRPCServer

# 调用函数
def respon_string(str):
    return "get string:%s"%str

class cpabe():
    def __init__(self):
        self.openabe = pyopenabe.PyOpenABE()
        self.cpabe = self.openabe.CreateABEContext("CP-ABE")
        self.cpabe.generateParams()
    def enc(self, message, policy):
        print("enc service is called.")
        ct = self.cpabe.encrypt(policy, message.data)
        return ct
    def dec(self, ct, username):
        key_path = "./keys/" + username + "_sk.txt"
        with open(key_path, "rb") as f:
            sk = f.read()
            f.close()
        self.cpabe.importUserKey(username, sk)
        print("ddkdk, ", type(ct), type(username))
        try:
            pt = self.cpabe.decrypt(username, ct.data)   # 解析返回错误，高优
            print("service dec pt =", pt)
            if pt == 0 or len(pt) < 2:
		 return b"DEC FAIL"
            return pt

        except Exception as e:
            print(e)
            return b"DEC FAIL0"
    def generate_userkey(self, username, userattri):

        try:
            self.cpabe.keygen(userattri, username)
        except:
            return "GENKEY FAIL"
        uk = self.cpabe.exportUserKey(username)
        # should write to db;
        filepath = "./keys/" + username + "_sk.txt"

        with open(filepath, 'wb') as f:
            f.write(uk)
            f.close()
        return uk





if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 8888)) # 初始化
    server.register_function(respon_string, "get_string") # 注册函数
    alg = cpabe()
    server.register_function(alg.enc, "cpabe_enc_cli")
    server.register_function(alg.dec, "cpabe_dec_cli")
    server.register_function(alg.generate_userkey, "cpabe_usrkey")

    print ("Listening for Client")
    server.serve_forever() # 保持等待调用状态
