
def convert_to_lowercase(string : str) -> str:
    '''
    A function to convert a string to lowercase
    '''
    try:
        #Create a variable to store the lowercase string
        lowercase_string : str = string.lower()
        #Returning lowercase string
        return lowercase_string
    except Exception as err:
        print(f'{err}')


print(convert_to_lowercase('BE A GOOD GIRL, federal!'))
