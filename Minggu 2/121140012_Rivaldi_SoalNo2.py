class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def enkripsi(self, plaintext):
        ciphertext = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                key_char = self.key[key_index % len(self.key)]
                key_index += 1
                shift = ord(key_char.upper()) - 65
                if char.isupper():
                    ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char
        return ciphertext

    def deskripsi(self, ciphertext):
        plaintext = ""
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                key_char = self.key[key_index % len(self.key)]
                key_index += 1
                shift = ord(key_char.upper()) - 65
                if char.isupper():
                    plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                plaintext += char
        return plaintext

key = input("Masukkan kata kunci: ")

cipher = VigenereCipher(key)

plaintext = input("Masukkan plaintext: ")

ciphertext = cipher.enkripsi(plaintext)

print("Ciphertext: ", ciphertext.upper())

plaintext = cipher.deskripsi(ciphertext)

print("Plaintext hasil dekripsi: ", plaintext)

