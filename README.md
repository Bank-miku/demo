# demo

## OpenFHE BGV encryption simulation

This repository now includes `bgv_openfhe_demo.cpp`, a step-by-step OpenFHE BGV example that prints output for:

1. Crypto context setup
2. Key generation
3. Message definition
4. Encoding to polynomial/plaintext form
5. Encryption
6. Decryption and decoding to original message

### Build (example)

> Make sure OpenFHE is installed and available on your system.

```bash
g++ -std=c++17 bgv_openfhe_demo.cpp -o bgv_openfhe_demo \
  -I/usr/local/include/openfhe \
  -L/usr/local/lib \
  -lopenfhe-pke -lopenfhe-core -lopenfhe-binfhe
```

### Run

```bash
./bgv_openfhe_demo
```
