from typing import List

def fibonacci_sequence(limit : int) -> List:
    '''
    A function to calculate the fibonacci sequence
    of numbers to a certain limit
    '''
    try:
        #Creating an empty list to store the sequence
        sequence : List = []
        #Creating a loop to compare the length of the sequence and the limit 
        while len(sequence) < limit:
            #setting the first number in the sequence to 1 if the limit is less than 2
            if len(sequence) < 2:
                sequence.append(1)
            else:
                #Calculating the numbers in the sequence
                sum_of_previous_two = sequence[-1] + sequence[-2]
                #Appending the next value to the sequence
                sequence.append(sum_of_previous_two)
        return sequence
    except Exception as err:
        print(f'{err}')


print(fibonacci_sequence(15))
