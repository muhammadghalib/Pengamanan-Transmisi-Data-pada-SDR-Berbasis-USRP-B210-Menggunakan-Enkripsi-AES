from Crypto.Cipher import AES
import binascii
import time
import os

def decrypt_aes_ecb(hex_string, secret_key):
    cipher = AES.new(secret_key, AES.MODE_ECB)
    encrypted_bytes = binascii.unhexlify(hex_string)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return decrypted_bytes.strip()

def read_and_decrypt_file(file_name, secret_key):
    with open(file_name, 'r') as f:
        for index, line in enumerate(f):
            hex_value = line.strip()
            try:
                decrypted_value = decrypt_aes_ecb(hex_value, secret_key)
                print("Baris {}: {}".format(index + 1, decrypted_value))
            except Exception:
                print("Baris {}: HEX not valid".format(index + 1))
            time.sleep(0.2)

if __name__ == "__main__":
    file_name = "receive_message.txt"

    # Kunci rahasia untuk dekripsi (harus sepanjang 16 byte)
    secret_key = "1111111111111111"

    read_and_decrypt_file(file_name, secret_key)