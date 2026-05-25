# Toy two-party BFV-to-TFHE ciphertext switching

This repository contains an educational prototype showing **masked decryption + re-encryption** from a toy BFV ciphertext into a toy TFHE ciphertext.

## What this demonstrates

Given a BFV ciphertext of `m mod P` with `P = 2^16`:

1. Alice samples a uniform random mask `r in Z_P`.
2. Alice adds `r` homomorphically in BFV, producing encryption of `m + r (mod P)`.
3. Alice computes a partial decryption share and sends only that share message to Bob.
4. Bob completes decryption and learns only `y = m + r (mod P)`.
5. Bob encrypts `y` under TFHE and sends it back.
6. Alice subtracts `r` homomorphically in TFHE to obtain encryption of `m`.

## Security intuition (toy setting)

- **Bob sees only `m + r mod P`**, not `m`, because `r` is unknown to Bob.
- **`r` must be uniform over `Z_P`** so that the masked value is information-theoretically hidden in this toy model.
- This is **not** a pure FHE key-switching-key approach; it is an **interactive masked decryption + re-encryption protocol**.
- A real system requires production-grade **threshold BFV** and **TFHE** implementations with robust parameterization, noise management, and security proofs.
- In real systems, **plaintext modulus and scaling/encoding between BFV and TFHE must be carefully matched**.

## Files

- `toy_bfv.py` – toy BFV context and threshold-style decryption shares.
- `toy_tfhe.py` – toy TFHE context and plaintext subtraction.
- `protocol.py` – two-party BFV-to-TFHE switching protocol.
- `main.py` – runnable demonstration.
- `test_protocol.py` – fixed and random-message tests.

## Run

```bash
python main.py
pytest
```

> ⚠️ Educational code only; do not use in production cryptography.
