# Fungsi untuk mengenkripsi pesan dengan Caesar Cipher
def encrypt_caesar(plaintext, shift):
    encrypted_text = ''
    
    # Loop untuk setiap karakter dalam plaintext
    for char in plaintext:
        # Mengecek apakah karakter adalah huruf
        if char.isalpha():
            # Mengatur batas huruf (upper atau lower case)
            offset = 65 if char.isupper() else 97
            # Menggeser karakter dan menambahkan ke hasil enkripsi
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Jika bukan huruf, tetap tambahkan karakter asli (misal spasi, tanda baca)
            encrypted_text += char
    
    return encrypted_text

# Fungsi untuk mendekripsi pesan dengan Caesar Cipher
def decrypt_caesar(ciphertext, shift):
    decrypted_text = ''
    
    # Loop untuk setiap karakter dalam ciphertext
    for char in ciphertext:
        # Mengecek apakah karakter adalah huruf
        if char.isalpha():
            # Mengatur batas huruf (upper atau lower case)
            offset = 65 if char.isupper() else 97
            # Menggeser karakter kembali untuk mendekripsi
            decrypted_text += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            # Jika bukan huruf, tetap tambahkan karakter asli
            decrypted_text += char
    
    return decrypted_text

# Input dari pengguna
plaintext = input("Masukkan pesan yang akan dienkripsi: ")
shift = int(input("Masukkan nilai pergeseran (shift): "))

# Mengenkripsi pesan
ciphertext = encrypt_caesar(plaintext, shift)
print(f"Hasil enkripsi: {ciphertext}")

# Mendekripsi pesan kembali
decrypted_text = decrypt_caesar(ciphertext, shift)
print(f"Hasil dekripsi: {decrypted_text}")
