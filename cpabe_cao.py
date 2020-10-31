from __future__ import print_function
import pyopenabe
import time
import rsa

def rsa_test():
    pubkey, privkey = rsa.newkeys(2048)
    msg = "hello"
    time0 = time.time()
    info = rsa.encrypt(msg.encode('utf-8'),pubkey)
    print("rsa enc time:", time.time()-time0)
    time1 = time.time()
    msg_dec = rsa.decrypt(info, privkey)
    print("rsa dec time:", time.time() - time1)
    print("dec result:", msg_dec)

def cpabe_test():
    print("Testing Python bindings for PyOpenABE...")

    openabe = pyopenabe.PyOpenABE()

    cpabe = openabe.CreateABEContext("CP-ABE")

    cpabe.generateParams()

    #cpabe.keygen("|two|three|", "alice")
    cpabe.keygen("Dept:SecurityResearch|level = 2| Company:ByteDance|Sex:female", "alice")

    pt1 = b"hello world!"
    # ct = cpabe.encrypt("((one or two) and three)", pt1)
    time_enc = time.time()
    ct = cpabe.encrypt("(((Dept:SecurityResearch) or (level >= 4 )) and (Company:ByteDance))", pt1)
    print("enc time:", time.time()-time_enc)

    print("ABE CT: ", len(ct))
    time_dec = time.time()
    pt2 = cpabe.decrypt("alice", ct)
    print("dec_time:", time.time()-time_dec)

    print("PT: ", pt2)
    assert pt1 == pt2, "Didn't recover the message!"

    print("Testing key import")

    msk = cpabe.exportSecretParams()
    mpk = cpabe.exportPublicParams()
    print("type mpk", type(mpk), mpk)
    uk = cpabe.exportUserKey("alice")
    with open("./mpk.txt", 'wb') as f:
        f.write((mpk))
        f.close()
    # print("alice sk:", uk)

    with open("./mpk.txt", 'rb') as f:
        mpk_load = f.read()
        f.close()
    # print("alice sk:", uk)
    cpabe2 = openabe.CreateABEContext("CP-ABE")

    print("mpl_load tyep:", type(mpk_load), type(mpk), len(mpk))
    #temp = bytes(mpk_load, encoding='utf-8')
    #print("tyem ypt:", type(temp), len(temp))


    cpabe2.importSecretParams(msk)
    cpabe2.importPublicParams(mpk_load)
    cpabe2.importUserKey("alice", uk)

    ct = cpabe2.encrypt("(((Dept:SecurityResearch) or (level >= 4 )) and (Company:ByteDance))", pt1)
    print("ABE CT: ", len(ct))

    pt2 = cpabe2.decrypt("alice", ct)
    print("PT: ", pt2)
    assert pt1 == pt2, "Didn't recover the message!"

    print("CP-ABE Success!")

if __name__ == '__main__':
   # rsa_test()
    cpabe_test()