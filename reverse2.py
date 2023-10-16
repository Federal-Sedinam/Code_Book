
def reverse(string : str) -> str:
    '''
    A function to reverse strings
    '''
    try:
        #An empty string to store the reversed string
        reversed_string : str = ''
        #Checking for the length of the string
        string_length : int = len(string)
        #Looping through the string
        for x in range(string_length):
            #Concantenating the reversed letter to the reversed string
            reversed_string += string[string_length-1]
            #Looping downwardly through the letters
            string_length -= 1
        #Returning the reversed string      
        return reversed_string
    except Exception as err:
        print(f'{err}')


print(reverse('Great'))
