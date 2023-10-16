from typing import List

def str_to_sorted_list(number_str : str) -> List:
    '''
    A function that converts an integer string to a list 
    '''
    try:
        #Create an empty empty list to store the list of integers
        number_list : List = []
        #Convert the string to a list and loop through the list
        #Seperate each element in the list using comma as the reference point for breaking
        for i in number_str.split(","):
            #Check if the element is an integer
            if get_int(i):
                #Append the element to the list if it's an integer
                number_list.append(int(i))
        #Arrange the new list in ascending order
        number_list.sort()
        #Return the new list
        return number_list
    except Exception as err:
        print(f'{err}')

def get_int(char : str) -> int:
    '''
    A function to handle the value error
    '''
    #Error handling
    try:
        return int(char)
    #Handle value error
    except Exception:
        #Do nothing
        pass


print(str_to_sorted_list("12,3,4,6,sdfg,e,sdf,wf,435,34563,45634,gf,t43,,31243,3,g,0,13"))
