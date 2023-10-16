
def reverse(string : str) -> str:
    '''
    A funtion to reverse the characters in a string
    '''
    try:
        #Reversing the letters and storing it
        reversed_string : str = string[::-1]
        #Returning the stored string
        return reversed_string
    except Exception as err:
        print(f'{err}')


print(reverse('I am Federal'))
