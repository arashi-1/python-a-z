import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)


#encrypted
plain_text = input("Enter the text: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Your original text : {plain_text}")
print(f"Encrypted_text  : {cipher_text}")     

#decrypted

cipher_text = input("Enter the encrypted text: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted_text  : {cipher_text}") 
print(f"Your original text : {plain_text}")
