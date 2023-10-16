def split(string : str) -> list:
    '''
    A function to split a string and sort out numbers from it
    '''
    try:
        #Create a variable to store the length of the string
        x : int = len(string)
        #Set the start index to zero
        start_index : int = 0
        #Set the end index to zero
        end_index : int= 0
        #Create an empty list to store the splited numbers
        numbers : list = []

        #Loop through the string using the index
        for index in range(x):
            #Check if the string is a comma
            if string[index] == ',':
                #End the split if it's a comma
                end_index = index
                #Extract the element from the string without redundant spaces
                substring =string[start_index:end_index].strip()
                #Check if the extracted element is a number
                if substring.isdigit():
                    #Append the element to the numbers list if it's a number
                    numbers.append(int(substring))
                #Start spliting again from the next element after the comma
                start_index = index + 1
        #Get last element from the string without any reduntant spaces
        last_element = string[start_index:].strip()
        #Check if last element is digit 
        if last_element.isdigit():
            #Append last element to the numbers list if it's a digit
            numbers.append(int(last_element))
        #Sorting the numbers in ascending order
        #numbers.sort()
        #Return the numbers      
        return bubble_sort(numbers)
    except Exception as err:
        print(f'{err}')
  
def bubble_sort(numbers : list) -> list:
    '''
    Function to sort numbers in ascending order
    '''
    try:
        numbers_len : int = len(numbers)
        for i in range(numbers_len - 1):
            position = 0
            for j in range(0, numbers_len-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
                    position = 1
                    if position == 0:
                        break
        return numbers
    except Exception as err:
        print(f'{err}')


print(split("12,3,4,6,sdfg,e,sdf,wf,435,34563,45634,gf,t43,,31243,3,g,0,13,g"))
