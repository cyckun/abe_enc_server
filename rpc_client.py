# -*- coding: utf-8 -*-
"""
    :author: Cao YongChao
    :mail: cyckun@aliyun.com
    :copyright: © 2020 Cao YongChao
    :license: MIT, see LICENSE for more details.
"""
from xmlrpc.client import ServerProxy

def cpabe_enc_cli(plain, policy):
    server = ServerProxy("http://localhost:8888") # 初始化服务器
    # print (server.get_string("oldboy_python6666")) # 调用函数并传参
    ct = server.cpabe_enc_cli(plain, policy)
    print("ct = ", ct)
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
    plain = b"hello rpc"   # must bytes format
    policy = "Dept:sec"

    with open("./sk.txt", "rb") as f:
        buffer = f.read()
        f.close()
    print("typeof buffer ", type(buffer))
    # ct = ""
    ct = cpabe_enc_cli(buffer, policy)
    print("ct type:", type(ct))
    with open("./pt.txt", "wb") as f:
        f.write(ct)
        f.close()
    with open("./ct.txt", "wb") as f:
        f.write(ct)
        f.close()

    sk = cpabe_userkey_cli("cyc1","Dept:sec")
    # print("sk = ", sk)
    with open("./ct.txt", "rb") as f:
        ct1 = f.read()
        f.close()
    pt = cpabe_dec_cli(ct1, "cyc1")
    print("pt = ", pt)
