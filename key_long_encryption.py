def encryption(message, key):
    enc_message = []
    for (letter, key_element) in zip(message, key):
        if letter.islower():
            shifted = (ord(letter) - ord("a") + int(key_element)) % 26 + ord("a")
            enc_message.append(chr(shifted))
        elif letter.isupper():
            shfited = (ord(letter) - ord("A") + int(key_element)) % 26 + ord("A")
            enc_message.append(shfited)
        else:
            enc_message.append(letter)

    return "".join(enc_message)

def decryption(message, key):
    dec_message = []
    for (letter, key_element) in zip(message, key):
        if letter.islower():
            shifted = (ord(letter) - ord("a") - int(key_element)) % 26 + ord("a")
            dec_message.append(chr(shifted))
        elif letter.isupper():
            shifted = (ord(letter) - ord("A") - int(key_element)) % 26 + ord("A")
            dec_message.append(chr(shifted))
        else:
            dec_message.append(letter)
    return "".join(dec_message)

def main():
    message = "hello"
    key_str = "2334421"
    key_str = (key_str * ((len(message) // len(key_str)) + 1))[:len(message)]
    print(f"Extended key: {key_str}")
    print(f"Encrypted message: {encryption(message, key_str)}")
    message_enc = encryption(message, key_str)
    print(f"Decrypted message: {decryption(message_enc, key_str)}")

main()
