# Note : Menggunakan hasil enkripsi heksadesimal jika menggunakan 
# alfabet (Sangat berisiko kehilangan informasi, dan ciphertext bisa tidak dapat dibaca atau dipetakan kembali dengan benar)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Fungsi untuk mengenkripsi pesan menggunakan AES dengan mode ECB
def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    # Padding dan enkripsi
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    # Mengonversi ciphertext ke format heksadesimal
    return ciphertext.hex()

# Fungsi untuk mendekripsi pesan menggunakan AES dengan mode ECB
def decrypt_aes(ciphertext_hex, key):
    # Mengonversi dari heksadesimal ke byte
    ciphertext = bytes.fromhex(ciphertext_hex)
    cipher = AES.new(key, AES.MODE_ECB)
    # Menghapus padding setelah dekripsi
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text.decode()

# Input dari pengguna
plaintext = input("Masukkan pesan yang akan dienkripsi: ")

# Membuat kunci secara acak (panjang 16 bytes untuk AES-128)
key = get_random_bytes(16)

# Mengenkripsi pesan
ciphertext_hex = encrypt_aes(plaintext, key)
print(f"Hasil enkripsi (ciphertext - hex): {ciphertext_hex}")

# Mendekripsi pesan
decrypted_text = decrypt_aes(ciphertext_hex, key)
print(f"Hasil dekripsi: {decrypted_text}")
