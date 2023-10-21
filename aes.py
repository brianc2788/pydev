#!/usr/bin/env python3
'''
aes.py
Using python's cryptography library to test the AES block cipher.
Updated code from Serious Cryptography by Jean-Phillipe Aumassen
from Python2 to Python3.
'''

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

# Generate random 16-byte key using crypto-safe linux PRNG.
k = urandom(16)
print(f'k = {hexa(k)}')

# Create an instance of AES-128 to encrypt a single block.
cipher = Cipher(algorithms.AES(k), modes.ECB(), backend = default_backend())
aes_encrypt = cipher.encryptor()

# Set plaintext block p to an all-zero string.
p = '\x00' * 16

# Encrypt plaintext p to ciphertext c.
c = aes_encrypt.update(p) + aes_encrypt.finalize()

print(f'enc({hexa(p)} = {hexa(c)}')

# Decrypt ciphertext back to plaintext.
aes_decrypt = cipher.decryptor()
p = aes_decrypt.update(c) + aes_decrypt.finalize()

print(f'dec({hexa(c)} = {hexa(p)}')

