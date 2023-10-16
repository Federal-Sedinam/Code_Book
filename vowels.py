
def removing_vowel(string: str) -> str:
    '''
    A funtions to remove all vowels from a string
    '''
    try:
        #An empty string to store the new string without the vowels
        new_string : str =''
        #Loop through the letters in the string
        for letter in string:
            #Get the ascii value of the string snd store it in the variable, 'ascii' 
            ascii : int = ord(letter)
            #Check if the ascii value of the string is that of a vowel
            if ascii == 97 or ascii == 101 or ascii == 105 or ascii == 111 or ascii == 117 or ascii == 65 or ascii == 69 or ascii == 73 or ascii == 79 or ascii == 85 :
                #Replace the letter with an empty space if it's a vowel
                new_string += letter.replace(letter, '')
            else:
                #Maintain the letter if it's not a vowel
                new_string += letter
        #Return the new  string 
        return new_string
    except Exception as err:
        print(f'{err}')


print(removing_vowel('A boy was born outside in the evening'))
