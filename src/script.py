class CryptoXOR:

    def crypto_xor(self, message: str, secret: str) -> str:
        new_chars = list()
        i = 0

        for num_chr in (ord(c) for c in message):
            num_chr ^= ord(secret[i])
            new_chars.append(num_chr)

            i += 1
            if i >= len(secret):
                i = 0

        return "".join(chr(c) for c in new_chars)

    def encrypt_xor(self, message: str, secret: str) -> str:
        return self.crypto_xor(message, secret).encode("utf-8").hex()

    def decrypt_xor(self, message_hex: str, secret: str) -> str:
        message = bytes.fromhex(message_hex).decode("utf-8")
        return self.crypto_xor(message, secret)
