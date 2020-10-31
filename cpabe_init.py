from __future__ import print_function
import pyopenabe
import time


def cpabe_init():
    print("Testing Python bindings for PyOpenABE...")

    openabe = pyopenabe.PyOpenABE()

    cpabe = openabe.CreateABEContext("CP-ABE")

    cpabe.generateParams()

    msk = cpabe.exportSecretParams()
    mpk = cpabe.exportPublicParams()
    with open("./mpk.txt", "wb") as f:
        f.write(mpk)
        f.close()
    with open("./msk.txt", "wb") as f:
        f.write(msk)
        f.close()

    print("CP-ABE Init Success!")

if __name__ == '__main__':
    cpabe_init()