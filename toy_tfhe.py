"""Toy TFHE-like primitives for educational protocol simulation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TFHECiphertext:
    """Toy ciphertext wrapper."""

    value: int


class TFHEContext:
    """Toy TFHE context with modular plaintext operations.

    Encryption/decryption are identity-style wrappers under modulus P to keep
    focus on protocol flow.
    """

    def __init__(self, plaintext_modulus: int = 2**16) -> None:
        self.P = plaintext_modulus

    def encrypt(self, m: int) -> TFHECiphertext:
        return TFHECiphertext(value=m % self.P)

    def decrypt(self, ct: TFHECiphertext) -> int:
        return ct.value % self.P

    def sub_plain(self, ct: TFHECiphertext, r: int) -> TFHECiphertext:
        return TFHECiphertext(value=(ct.value - (r % self.P)) % self.P)
