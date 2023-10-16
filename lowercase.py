
def convert_to_lowercase(string : str) -> str:
    '''
    A function to convert the letters in a string to lowercase
    '''
    try:
        #Creating an empty string to store the lowercase string
        lowercase_string : str = ''
        #Looping through the sentence to find uppercase characters
        for character in string:
            #Converting the characters to ascii values
            ascii : int = ord(character)
            #Checking if ascii value is that of an uppercase or lowercase
            if ascii >= 65 and ascii <= 90:
                #Converting the uppercase to lowercase and appending it to empty string
                lowercase_string += chr(ascii + 32)
            else:
                #Appending lowercase characters to empty string
                lowercase_string += chr(ascii)
        #Returning the lowercases
        return lowercase_string
    except Exception as err:
        print(f'{err}')
    

print(convert_to_lowercase('BE A GOOD GIRL, federal!'))
