"""Toy BFV-like primitives for educational protocol simulation.

This module intentionally uses simplified arithmetic and should never be used
for real cryptographic purposes.
"""

from __future__ import annotations

from dataclasses import dataclass
import secrets
from typing import Dict


@dataclass
class BFVCiphertext:
    """Toy ciphertext containing two components modulo plaintext modulus."""

    c0: int
    c1: int


class BFVContext:
    """Toy two-party BFV context with additive secret sharing.

    We model a ciphertext as:
        c0 = m + noise - a*s
        c1 = a
    so decryption is c0 + c1*s = m + noise (mod P).

    To keep tests deterministic and exact, encryption chooses zero noise.
    """

    def __init__(self, plaintext_modulus: int = 2**16) -> None:
        self.P = plaintext_modulus
        # Secret key is split as s = s_alice + s_bob mod P.
        self.s_alice = secrets.randbelow(self.P)
        self.s_bob = secrets.randbelow(self.P)
        self.s = (self.s_alice + self.s_bob) % self.P
        # Internal protocol state for a single conversion call.
        self._pending_mask: int | None = None

    def encrypt(self, m: int) -> BFVCiphertext:
        """Encrypt plaintext m modulo P under the toy BFV scheme."""
        m_mod = m % self.P
        a = secrets.randbelow(self.P)
        noise = 0
        c1 = a
        c0 = (m_mod + noise - (a * self.s)) % self.P
        return BFVCiphertext(c0=c0, c1=c1)

    def add_plain(self, ct: BFVCiphertext, r: int) -> BFVCiphertext:
        """Homomorphically add a plaintext mask r to ciphertext."""
        r_mod = r % self.P
        return BFVCiphertext(c0=(ct.c0 + r_mod) % self.P, c1=ct.c1)

    def partial_decrypt_alice(self, ct: BFVCiphertext) -> Dict[str, int]:
        """Alice's threshold partial decryption output.

        Returns a message for Bob that includes Alice's partial share and the
        masked ciphertext component needed to complete decryption.
        """
        d_alice = (ct.c1 * self.s_alice) % self.P
        return {"c0": ct.c0, "c1": ct.c1, "d_alice": d_alice}

    def complete_decrypt_bob(self, partial: Dict[str, int]) -> int:
        """Bob completes threshold decryption from Alice's partial."""
        c0 = partial["c0"] % self.P
        c1 = partial["c1"] % self.P
        d_alice = partial["d_alice"] % self.P
        d_bob = (c1 * self.s_bob) % self.P
        return (c0 + d_alice + d_bob) % self.P
