
def convert_to_uppercase(string : str) -> str:
    '''
    A function to convert the letters in a string to uppercase
    '''
    try:
        #Creating an empty string to store the uppercase string
        uppercase_string : str = ''
        #Looping through the sentence to find lowecase characters
        for character in string:
            #Converting the characters to ascii values
            ascii : int = ord(character)
            #Checking if ascii value is that of an uppercase or lowercase
            if ascii >= 97 and ascii <= 122:
                #Converting the lowercase to upper case and appending it to empty string
                uppercase_string += chr(ascii - 32)
            else:
                #Appending uppercase character to empty string
                uppercase_string += chr(ascii)
        #Returning the uppercases
        return uppercase_string
    except Exception as err:
        print(f'{err}')


print(convert_to_uppercase('be a good girl, FEDERAL!'))
