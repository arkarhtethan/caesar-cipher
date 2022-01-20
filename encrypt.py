letters = ['a', 'b', 'c', 'd', 'e']


def encrypt(data, key):
    result = ""
    LOWER_CASE_START = 97
    TOTAL_ALPHABET = 26
    data = data.lower()
    for x in data:
        result += chr((ord(x)+int(key) - LOWER_CASE_START) %
                      TOTAL_ALPHABET + LOWER_CASE_START)

    return result


run = "y"

while run == "y":

    inputText = input("\nEnter Plain Text : ")
    key = input("Enter key : ")
    if not key.isdigit():
        print("Key must be digit")
        continue

    result = encrypt(inputText, key)

    print(f'Plaintext : {inputText.upper()}')
    print(f'Cipher Text : {result.upper()}')

    run = input("\nPress y to run again : ")
