from typing import List

def remove_vowel(string : str) -> str:
    '''
    A function that removes all vowels from a string
    '''
    try:
        #An empty string to store the new string
        new_string : str = ''
        #A list of all vowels
        vowels : list = ['a', 'e','i', 'o', 'u']
        #Convert all vowels to uppercase and store it in uppercase vowels
        uppercase_vowels = [character.upper() for character in vowels]
        #Loop through the letters in the string
        for letter in string:
            #Check if the letter is a either a lowercase vowel or an uppercase
            if letter in vowels or letter in uppercase_vowels:
                #Replace the letter with an empty space if it's a vowel
                new_string += letter.replace(letter, '')
            else:
                #Maintain the string if it's not a vowel
                new_string += letter
                #Return the new string
        return new_string
    except Exception as err:
        print(f'{err}')


print(remove_vowel('A boy was born outside this evening'))
