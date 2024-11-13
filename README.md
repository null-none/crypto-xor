# crypto-xor
Encrypt-decrypt string with your password


### Install

```bash
pip install crypto-xor
```

### Example

```python

from crypro_xor.script import CryptoXOR

crypto_xor = CryptoXOR()
encrypted = crypto_xor.encrypt_xor(message="hello world", secret="Password123!")
print(encrypted)
# g197d189d18bd192d18ed18bd08cd081d1b3d19dd16d
decrypted = crypto_xor.decrypt_xor(message="g197d189d18bd192d18ed18bd08cd081d1b3d19dd16d", secret="Password123!")
print(decrypted)
# hello world
```