from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

input_file = "send_message.txt"
output_file = "encrypted_send_message.txt"

# Secret Key (harus 16, 24, atau 32 byte)
secret_key = b"1111111111111111"[:16]

with open(input_file, "r") as file:
    plaintext = file.read()

cipher = AES.new(secret_key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

with open(output_file, "w") as file:
    file.write(binascii.hexlify(ciphertext).decode('utf-8') + "\n")

print("Pesan dari '{}' telah berhasil dienkripsi dan disimpan di '{}'.".format(input_file, output_file))
