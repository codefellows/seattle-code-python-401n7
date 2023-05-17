# Plaintext: "1239"
# Key: 2
# Ciphertext: "3451"


def encrypt(plaintext, key):
    """
    Takes in a string of integers representing the plaintext. Returns a new string of integers representing the
    ciphertext. Shifts plaintext ints by key, and using the modulo % operator
    :param plaintext: String of ints
    :param key: Int
    :return: String of ints
    """
    # Input "1239", 2
    ciphertext = ""

    # some sort of interation through the plaintext
    for number in plaintext:
        # build up the ciphertext one character at a time
        number = int(number)   # "1" -> 1
        shift_number = (number + key) % 10  # (9 + 2) % 10 -> 1
        ciphertext += str(shift_number)

    return ciphertext
    # return "3451


def decrypt(ciphertext, key):
    """
    Reverses the encrypt() operation.
    :param ciphertext: String of ints
    :param key: Int representing the original shift
    :return: String of ints
    """
    plaintext = ""

    # some sort of interation through the ciphertext
    for number in ciphertext:
        # build up the plaintext one character at a time
        number = int(number)   # "1" -> 1
        shift_number = (number + (10 - key)) % 10  # (5 + (10 - 7)) % 10 -> 8
        plaintext += str(shift_number)

    return plaintext
    # return encrypt(ciphertext, -key)


if __name__ == "__main__":
    phone_number = "8005551234"
    secret_number = encrypt(phone_number, 7)
    print("the secret_number is:", secret_number)

    # How do I reverse the process?
    decrypted_number = decrypt(secret_number, 7)
    print("the decrypted secret_number is:", decrypted_number)
