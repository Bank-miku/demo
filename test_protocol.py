import random

from protocol import bfv_to_tfhe_two_party_switch
from toy_bfv import BFVContext
from toy_tfhe import TFHEContext


P = 2**16


def run_roundtrip(m: int) -> int:
    bfv = BFVContext(plaintext_modulus=P)
    tfhe = TFHEContext(plaintext_modulus=P)
    ct_bfv = bfv.encrypt(m)
    ct_tfhe = bfv_to_tfhe_two_party_switch(ct_bfv, bfv, tfhe)
    return tfhe.decrypt(ct_tfhe)


def test_fixed_messages() -> None:
    for m in [0, 1, 42, 12345, 65535]:
        assert run_roundtrip(m) == m % P


def test_random_messages() -> None:
    rng = random.Random(0)
    for _ in range(100):
        m = rng.randrange(0, P)
        assert run_roundtrip(m) == m % P
