from __future__ import print_function
import pyopenabe
from flask import current_app
import time


def cpabe_dec():
    print("Testing Python bindings for PyOpenABE...")

    openabe = pyopenabe.PyOpenABE()

    cpabe = openabe.CreateABEContext("CP-ABE")
    usr_id = "bob"
    mpk = b'0'
    uk = b'0'
    with open("./mpk.txt", "rb") as f:
        mpk = f.read()
        f.close()
    cpabe.importPublicParams(mpk)

    with open("./bob_key.txt", "rb") as f:
        uk = f.read()
        f.close()
    cpabe.importUserKey(usr_id, uk)

    with open("./alice_ct.txt", "rb") as f:
        ct = f.read()
        f.close()



    time_dec = time.time()
    pt2 = cpabe.decrypt(usr_id, ct)
    print("dec_time:", time.time()-time_dec)
    print("bob dec result:", pt2)
    print("CP-ABE dec!")

def cpabe_dec_cli(ct, user_name):
    print("Testing Python bindings for PyOpenABE...")

    openabe = pyopenabe.PyOpenABE()
    cpabe = openabe.CreateABEContext("CP-ABE")
    usr_id = "bob"
    mpk = b'0'
    uk = b'0'

    key_path = current_app.config['ABE_KEYS_PATH'] + "/mpk.txt"

    print("key paht :", key_path)
    with open(key_path, "rb") as f:
        mpk = f.read()
        f.close()
    cpabe.importPublicParams(mpk)

    user_sk_path = current_app.config['ABE_KEYS_PATH'] + "/" + user_name + "_sk.txt"
    with open(user_sk_path, "rb") as f:
        uk = f.read()
        f.close()
    cpabe.importUserKey(usr_id, uk)


    time_dec = time.time()
    try:
        pt2 = cpabe.decrypt(usr_id, ct)   # 解析返回错误，高优

        print("dec_time:", time.time()-time_dec)
        # print("bob dec result:", pt2)
        print("CP-ABE dec!")
        return pt2
    except:
        return "DEC FAIL"

if __name__ == '__main__':
    cpabe_dec()