def encrypt(message, key):
    ascii_message = []
    ascii_message_encrypt = []
    encrypted_message = []
    for letter in message.lower():
        ascii_message.append(ord(letter))
    for ascii_letter in ascii_message:
        if ascii_letter != 122:
            ascii_message_encrypt.append(ascii_letter + key)
        else:
            ascii_message_encrypt.append(97 + key - 1)
    for encrypted_ascii in ascii_message_encrypt:
        encrypted_message.append(chr(encrypted_ascii))
    return str(encrypted_message)


def main():
    message = "abcz"
    key = 1
    print(encrypt(message, key))


main()
