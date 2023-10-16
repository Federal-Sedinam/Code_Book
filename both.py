def convert_to_uppercase_and_lowercase(string : str) -> str:
    '''
    A  function to convert lowercase string to upercase and uppercase to lowercase 
    '''
    try:
        #Creating an empty string to store the converted characters
        converted_string : str = ''
        #Looping through characters 
        for character in string:
            #Converting characters into ascii codes 
            ascii : int = ord(character)
            #A condition to check if character is in lowercase
            if ascii >= 97 and ascii <= 122:
                #Converting character to uppercase            
                converted_string += character.upper()
            #A condition to check if character is uppercase
            elif ascii >= 65 and ascii <= 90:
                #Converting character to lowercase 
                converted_string += character.lower()
            #Checking for other cases 
            else:
                #Default conditions for other cases
                converted_string +=' '
        #Returning converted string        
        return converted_string
    except Exception as err:
        print(f'{err}')


print(convert_to_uppercase_and_lowercase('PLEASE how ARE you DOING?'))
