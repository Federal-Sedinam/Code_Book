from typing import List

def get_even_numbers(number_list : list) -> list:
    '''
    A funtion to sort out even numbers from a 
    list of numbers and return the list of even numbers
    '''
    try:
        # Creating an empty list to contain even numbers
        even_numbers: list = []
        #Looping through the list of numbers to find even numbers
        for number in number_list:
            #Checking if number is even or not
            if number % 2 == 0:
                #Appending the even numbers to the created list
                even_numbers.append(number)
        #Returning the even numbers 
        return even_numbers
    except Exception as err:
        print(f'{err}')


print(get_even_numbers([3,4,6,6,5,4,5,3]))
