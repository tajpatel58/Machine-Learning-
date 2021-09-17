

import enchant

with open('p059_cipher.txt','r') as f:
    for line in f:
        encrypted_msg = line


encrypted_msg = encrypted_msg.split(",")

for j in range(0, len(encrypted_msg)):
    encrypted_msg[j] = int(encrypted_msg[j])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet = list(alphabet)

d = enchant.Dict("en_GB")

def decrypt(encrypted_text, key):
    key_length = len(key)
    key_ascii = [0] * key_length
    for k in range(0, key_length):
        key_ascii[k] = ord(key[k])
    decrypted_text = ""
    for j in range(0,len(encrypted_text)):
        index_for_key = j % key_length
        decrypted_text = decrypted_text + chr(encrypted_text[j] ^ key_ascii[index_for_key])
    return decrypted_text


def decrypted_ascii(encrypted_text,key):
    key_length = len(key)
    key_ascii = [0]*key_length
    decrypt_array = [0]*len(encrypted_text)
    for j in range(0, key_length):
        key_ascii[j] = ord(key[j])
    for i in range(0, len(encrypted_text)):
        key_index = i % key_length
        decrypt_array[i] = int(encrypted_text[i] ^ key_ascii[key_index])
    return decrypt_array





# Here we get given some encrypted text and try to comoute a key given that it's 3 letters. We do this by brute force, ie
# Cycling through all possible keys, then we use the fact that we know the output are real english words.
# The below will list all the keys that have the first 2 words of the decrypted message as real english words.
# Note we classify words as before and after the space.

def key_finder(encrypted_text):
    keys = [] # This array will hold all keys with first 2 words as real english words
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                key_test = [a, b, c]
                array_decrypt = decrypt(encrypted_text,key_test).split(" ")
                if d.check(array_decrypt[0]) == True and d.check(array_decrypt[1]) == True:
                    keys.append(key_test)
                else:
                    continue
    # Once we have all keys that have first 2 words as english, then we check if 3rd word is english, then 4th etc.
    # Keep doing this until only one remains.
    while len(keys) != 1:
        word_checker = 2
        for key in keys:
            array_decrypt = decrypt(encrypted_text, key).split(" ")
            if d.check(array_decrypt[word_checker]) == True:
                continue
            else:
                keys.remove(key)
        word_checker += 1
    correct_key = keys[0]
    return sum(decrypted_ascii(encrypted_text,correct_key))


print(key_finder(encrypted_msg))
