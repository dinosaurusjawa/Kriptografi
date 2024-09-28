import random

# Fungsi untuk mengenkripsi pesan menggunakan teknik permutasi
def encrypt_permutation(plaintext, key):
    # Membagi plaintext menjadi blok-blok dengan ukuran sesuai dengan panjang kunci
    block_size = len(key)
    blocks = [plaintext[i:i+block_size] for i in range(0, len(plaintext), block_size)]
    
    # Jika blok terakhir tidak penuh, tambahkan padding (spasi) agar sesuai dengan ukuran blok
    if len(blocks[-1]) < block_size:
        blocks[-1] += ' ' * (block_size - len(blocks[-1]))

    ciphertext = ''
    # Melakukan permutasi pada setiap blok
    for block in blocks:
        permuted_block = ''.join([block[i] for i in key])
        ciphertext += permuted_block
    return ciphertext

# Fungsi untuk mendekripsi pesan yang dienkripsi menggunakan teknik permutasi
def decrypt_permutation(ciphertext, key):
    # Membagi ciphertext menjadi blok-blok dengan ukuran sesuai dengan panjang kunci
    block_size = len(key)
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    
    decrypted_text = ''
    # Inversi permutasi berdasarkan kunci
    inverse_key = [0] * len(key)
    for i, pos in enumerate(key):
        inverse_key[pos] = i

    # Mengembalikan permutasi ke urutan semula
    for block in blocks:
        original_block = ''.join([block[i] for i in inverse_key])
        decrypted_text += original_block
    return decrypted_text.strip()

# Input dari pengguna
plaintext = input("Masukkan pesan yang akan dienkripsi: ")

# Membuat kunci permutasi secara acak
block_size = 4  # Panjang blok (misalnya 4 karakter per blok)
key = list(range(block_size))
random.shuffle(key)

# Mengenkripsi pesan
ciphertext = encrypt_permutation(plaintext, key)
print(f"Hasil enkripsi (ciphertext): {ciphertext}")

# Mendekripsi pesan
decrypted_text = decrypt_permutation(ciphertext, key)
print(f"Hasil dekripsi: {decrypted_text}")
