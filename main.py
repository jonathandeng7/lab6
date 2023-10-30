

#encoding function
def encoder(password):
    encoded_password = ''
    for i in password:
        value = int(i) + 3
        if value >= 10:
            value -= 10
        encoded_password += str(value)

    return encoded_password

#menu function
def menu():
    print("Menu")
    print("-"*13)
    print("1. Encoder")
    print("2. Decoder")
    print("3. Quit")






#decoder function
def decoder(encoded_password):
    decoded_password = ""
    for i in encoded_password:
        if int(i) <= 2:
            value = int(i) + 7
        else:
            value = int(i) - 3
        decoded_password += str(value)
    return decoded_password

#menu selection
if __name__ == '__main__':
    menu_selection = 0
    #checks whether or not to quit the program
    while menu_selection != 3:
        menu()
        menu_selection = int(input("Please enter an option: "))
        #if the user chooses to encode
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored")
        #if the user chooses to decode
        elif menu_selection == 2:
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")

