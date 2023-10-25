password = input("Enter an 8-digit password: ")

def encoder(password):
    encoded_password = ''
    for i in password:
        value = int(i) + 3
        if value >= 10:
            value -= 10
        encoded_password += str(value)

    return encoded_password

print(encoder(password))