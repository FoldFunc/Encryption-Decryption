def encrypt(message, key):
    encrypted_message = []
    for letter in message:
        if letter.islower():
            shifted = (ord(letter) - ord("a") + key) % 26 + ord('a')
            encrypted_message.append(chr(shifted))
        elif letter.isupper():
            shifted = (ord(letter) - ord("A") + key) % 26 + ord('A')
            encrypted_message.append(chr(shifted))
        else:
            encrypted_message.append(letter)
    return "".join(encrypted_message)
def decrypt(encrypted_message, key):
    message = []
    for letter in encrypted_message:
        if letter.islower():
            shifted = (ord(letter) - ord('a') - key) % 26 + ord('a')
            message.append(chr(shifted))
        elif letter.isupper():
            shifted = (ord(letter) - ord('A') - key) % 26 + ord('A')
            message.append(chr(shifted))
        else:
            message.append(letter)
    return ''.join(message)
def main():
    message = "abczy"
    key = 2
    encrypted_message = encrypt(message, key)
    print(encrypted_message)
    message_decrypted = decrypt(encrypted_message, key)
    print(message_decrypted)



main()
