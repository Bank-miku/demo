#include "openfhe.h"

#include <iostream>
#include <vector>

using namespace lbcrypto;

int main() {
    std::cout << "=== BGV Encryption Scheme Simulation with OpenFHE ===\n\n";

    // 1) Context generation (BGV parameters)
    std::cout << "[1/6] Create crypto context for BGV\n";
    CCParams<CryptoContextBGVRNS> parameters;
    parameters.SetPlaintextModulus(65537);
    parameters.SetMultiplicativeDepth(2);
    parameters.SetBatchSize(16);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);

    cc->Enable(PKE);
    cc->Enable(KEYSWITCH);
    cc->Enable(LEVELEDSHE);

    std::cout << "    Plaintext modulus: " << parameters.GetPlaintextModulus() << "\n";
    std::cout << "    Multiplicative depth: " << parameters.GetMultiplicativeDepth() << "\n";
    std::cout << "    Batch size: " << parameters.GetBatchSize() << "\n\n";

    // 2) Key generation
    std::cout << "[2/6] Key generation\n";
    auto keyPair = cc->KeyGen();
    if (!keyPair.good()) {
        std::cerr << "    Key generation failed.\n";
        return 1;
    }
    std::cout << "    Public and secret keys generated successfully.\n\n";

    // 3) Input message
    std::vector<int64_t> message = {12, 45, 90, 7, 1, 0, 33, 88};
    std::cout << "[3/6] Original message\n";
    std::cout << "    m = [ ";
    for (const auto& v : message) {
        std::cout << v << " ";
    }
    std::cout << "]\n\n";

    // 4) Encode message to polynomial/plaintext form
    std::cout << "[4/6] Encode message to polynomial/plaintext form\n";
    Plaintext pt = cc->MakePackedPlaintext(message);
    std::cout << "    Encoded plaintext polynomial: " << pt << "\n\n";

    // 5) Encryption
    std::cout << "[5/6] Encryption phase\n";
    auto ciphertext = cc->Encrypt(keyPair.publicKey, pt);
    std::cout << "    Ciphertext generated successfully.\n\n";

    // 6) Decryption + decoding
    std::cout << "[6/6] Decryption phase and decode to original message\n";
    Plaintext decrypted;
    cc->Decrypt(keyPair.secretKey, ciphertext, &decrypted);
    decrypted->SetLength(message.size());

    std::cout << "    Decrypted plaintext polynomial: " << decrypted << "\n";

    auto decoded = decrypted->GetPackedValue();
    std::cout << "    Decoded message = [ ";
    for (const auto& v : decoded) {
        std::cout << v << " ";
    }
    std::cout << "]\n\n";

    std::cout << "=== Verification ===\n";
    if (decoded == message) {
        std::cout << "SUCCESS: Decoded message matches the original message.\n";
    } else {
        std::cout << "FAIL: Decoded message does NOT match the original message.\n";
    }

    return 0;
}
