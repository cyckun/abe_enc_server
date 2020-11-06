# -*- coding: utf-8 -*-
"""
    :author: Cao YongChao
    :mail: cyckun@aliyun.com
    :copyright: © 2020 Cao YongChao
    :license: MIT, see LICENSE for more details.
"""
import time
from xmlrpc.client import ServerProxy

def cpabe_enc_cli(plain, policy):
    server = ServerProxy("http://localhost:8888") # 初始化服务器
    # print (server.get_string("oldboy_python6666")) # 调用函数并传参
    ct = server.cpabe_enc_cli(plain, policy)
    # print("ct = ", ct)
    return ct.data
def cpabe_dec_cli(ct, username):
    server = ServerProxy("http://localhost:8888") # 初始化服务器
    # print (server.get_string("oldboy_python6666")) # 调用函数并传参
    pt = server.cpabe_dec_cli(ct, username)
    return pt.data
def cpabe_userkey_cli(username, userattri):
    server = ServerProxy("http://localhost:8888")  # 初始化服务器
    # print (server.get_string("oldboy_python6666")) # 调用函数并传参
    sk = server.cpabe_usrkey(username, userattri)
    return sk.data   # whether sk is returned, think lator;


if __name__ == '__main__':
    plain1 = b"hello rpc999999999999999999999999999999999999999999999999999999999999999999999"
    with open("./test.txt", "rb") as f:
        plain = f.read()
        f.close()

    policy = test_policy_count(1000)
    print("policy = ", policy)
    #policy = "((Name:sec) or (Name:cyc))"
    # print("ret = ", policy1)

    with open("./pt.txt", "rb") as f:
        buffer = f.read()
        f.close()
    print("typeof buffer ", type(buffer))
    # ct = ""
    begin = time.time()
    ct = cpabe_enc_cli(plain, policy)
    print("enc_time:", time.time()-begin)
    print("ct len:", len(ct))
    ''''
    with open("./ct.txt", "wb") as f:
        f.write(ct)
        f.close()
    '''
    sk = cpabe_userkey_cli("cyc1","Name:cao3")
    # print("sk = ", sk)
    '''
    with open("./ct.txt", "rb") as f:
        ct1 = f.read()
        f.close()
    '''
    dec_time = time.time()
    pt = cpabe_dec_cli(ct, "cyc1")
    end = time.time()
    # print("pt = ", pt)
    print("dec_time = ", end-dec_time)
