from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

load_dotenv()
print(os.getenv("AES_KEY"))

key = get_random_bytes(32)
print(key)
print(key.hex())
target_data="4562123456780000"

cipher = AES.new(key, AES.MODE_ECB)
enc_result = cipher.encrypt(b'4562123456780000')
print(enc_result)
print(enc_result.hex())

dec_cipher = AES.new(key, AES.MODE_ECB)
dec_result = dec_cipher.decrypt(enc_result)
print(dec_result)






