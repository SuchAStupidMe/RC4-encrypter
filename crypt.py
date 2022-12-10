from arc4 import ARC4


def rc4_encrypt(password, file):
    arc4 = ARC4(bytes(password, 'utf-8'))
    with open(file, 'rb')as read:
        cipher = arc4.encrypt(read.read())
        with open(file, 'wb') as save:
            save.write(cipher)
        return "Encryption successful"


def rc4_decrypt(password, file):
    arc4 = ARC4(bytes(password, 'utf-8'))
    with open(file, 'rb')as read:
        cipher = arc4.decrypt(read.read())
        with open(file, 'wb') as save:
            save.write(cipher)
        return "Decryption successful"
