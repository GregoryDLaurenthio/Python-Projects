import random
message = "Hello, world!"
shift = random.randint (1,7)

FIRST_ASCII_CHAR_CODE = ord ("A")
LAST_ASCII_CHAR_CODE = ord ("Z")
ASCII_CHAR_RANGE = LAST_ASCII_CHAR_CODE - FIRST_ASCII_CHAR_CODE + 1

def caesar_shift (message, shift):
    # result placeholder
    result = ""

    #Goes through each letter of the message
    for char in message.upper ():
        if char.isalpha():
            #converts character to its ASCII code
            char_code = ord(char)
            new_char_code = char_code + shift

            #limits the ascii charset used to only feature alphabetical characters
            if new_char_code > LAST_ASCII_CHAR_CODE:
                new_char_code -=ASCII_CHAR_RANGE

            if new_char_code < FIRST_ASCII_CHAR_CODE:
                new_char_code +=ASCII_CHAR_RANGE

            #converts ascii code back into words
            new_char = chr(new_char_code)

            #appends result one by one
            result += new_char

        else:
            #appends original characters that are not alphabetical
            result += char

    print (result)

def start_program ():
    #loops the program for multiple use
    while True:
        #user option to encrypt or decrypt
        setup_input = input("Encrypt [1] or Decrypt [2]?\n")

        #user input for variables to translate
        user_input = input("\nEnter Message to be processed\n")

        encrypt = ["encrypt","1","[2]"]
        decrypt = ["decrypt","2","[2]"]
        end_program = ["end"]

        if user_input.lower () in end_program:
            break

        if setup_input.lower() in encrypt:
            user_shift_input = input ("Enter SHIFT value\n")

            #confirms that user input is a digit
            if user_shift_input.isdigit ():
                user_shift = int(user_shift_input)

                #calls caesar_shift function for translation
                caesar_shift (user_input, user_shift)
                pause_input = input ("\nOK?\n")

            else:
                user_shift_input = input ("Enter SHIFT value\n")

        if setup_input.lower() in decrypt:
            user_shift_input = input ("Enter SHIFT value\n")
            if user_shift_input.isdigit ():
                user_shift = int(user_shift_input)
                user_shift -= (user_shift *2)
                caesar_shift (user_input, user_shift)
                pause_input = input("\nOK?\n")
            else:
                user_shift_input = input ("Enter SHIFT value\n")

        else:
            print ("error occurred, please retype answer...\n")

#initializing program
start_program ()