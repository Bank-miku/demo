"""Two-party BFV-to-TFHE masked decryption + re-encryption prototype."""

from __future__ import annotations

import secrets

from toy_bfv import BFVCiphertext, BFVContext
from toy_tfhe import TFHECiphertext, TFHEContext


def bfv_to_tfhe_two_party_switch(
    ct_bfv: BFVCiphertext,
    bfv_ctx: BFVContext,
    tfhe_ctx: TFHEContext,
) -> TFHECiphertext:
    """Convert BFV ciphertext to TFHE ciphertext via two-party interaction.

    Alice role:
      1) sample mask r
      2) mask BFV ciphertext by adding r
      3) produce partial decryption and send to Bob

    Bob role:
      4) complete decryption to obtain y = m+r
      5) re-encrypt y under TFHE and send to Alice

    Alice role:
      6) remove mask homomorphically in TFHE to recover encryption of m
    """
    P = bfv_ctx.P

    # Alice: pick uniform random mask over Z_P, keep private.
    r = secrets.randbelow(P)
    ct_bfv_masked = bfv_ctx.add_plain(ct_bfv, r)
    partial = bfv_ctx.partial_decrypt_alice(ct_bfv_masked)

    # Bob: sees only masked plaintext y.
    y = bfv_ctx.complete_decrypt_bob(partial)
    ct_tfhe_masked = tfhe_ctx.encrypt(y)

    # Alice: remove mask in TFHE domain.
    ct_tfhe = tfhe_ctx.sub_plain(ct_tfhe_masked, r)
    return ct_tfhe
