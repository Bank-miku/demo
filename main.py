from toy_bfv import BFVContext
from toy_tfhe import TFHEContext
from protocol import bfv_to_tfhe_two_party_switch


def main() -> None:
    P = 2**16
    bfv = BFVContext(plaintext_modulus=P)
    tfhe = TFHEContext(plaintext_modulus=P)

    m = 12345
    ct_bfv = bfv.encrypt(m)
    ct_tfhe = bfv_to_tfhe_two_party_switch(ct_bfv, bfv, tfhe)
    recovered = tfhe.decrypt(ct_tfhe)

    print(f"Original message: {m % P}")
    print(f"Recovered message after BFV->TFHE switch: {recovered}")


if __name__ == "__main__":
    main()
