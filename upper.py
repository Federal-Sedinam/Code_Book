
def convert_to_uppercase(string : str):
    '''
    A function to convert the letters in a string to uppercase
    '''
    try:
        #Appending uppercase string
        uppercase_string : str = string.upper()
        #Returning uppercase
        return uppercase_string
    except Exception as err:
        print(f'{err}')


print(convert_to_uppercase('be a good girl, FEDERAL!'))
