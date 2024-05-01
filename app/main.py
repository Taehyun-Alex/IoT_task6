from app.encrypt import Encryptor
from app.decrypt import Decryptor

file_name = "../files/original.txt"
encrypted_name = "../files/encrypted.txt"
decrypted_name = "../files/decrypted.txt"


class FileAdapter:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, "r") as f:
            result = f.read()
            return result


enc = Encryptor("avocadoisthekey")
with open(encrypted_name, "wb") as f_encrypted:
    f_encrypted.write(enc.encrypt(FileAdapter(file_name).read_data()))

dec = Decryptor("avocadoisthekey")
with open(decrypted_name, "wb") as f_decrypted:
    f_decrypted.write(dec.decrypt(FileAdapter(encrypted_name).read_data()))

with open(file_name, "r") as f, open(decrypted_name, "r") as d:
    original_content = f.read()
    decrypted_content = d.read(
    )

if original_content == decrypted_content:
    print("[Decryption successful] Contents match")
else:
    print("[Decryption failed] Contents do not match")




