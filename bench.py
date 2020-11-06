from rpc_client import cpabe_enc_cli, cpabe_dec_cli, cpabe_userkey_cli
import time


def test_policy_count(count):
    init_policy = "Name:cao"
    policy = ""
    i = 0
    while i < count -1 :
        temp = "(" + init_policy + str(i) + ") "
        policy += temp + "or"
        i +=1
    temp = "(" + init_policy + str(count) + ") "
    policy += temp
    return policy

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