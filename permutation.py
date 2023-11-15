def permutation(word):
    '''
    A function to generate all possible permutations of characters from a given word.
    '''
    # Create an empty list to store all possible permutations
    result = []
    # Check if the word is a one letter word or an empty string
    if len(word) <= 1:
        # Return the word as a list
        return [word]
    # Iterate through the characters of the word
    for character in word:
        # Generate permutations for the remaining characters recursively
        current_word = permutation(word.replace(character, ""))
        # Iterate through the permutations of the remaining characters
        for letter in current_word:
            # Combine the current character with each permutation
            new_words = character + letter
            # Add the new combination to the result list
            result.append(new_words)
    # Return the list of all permutations
    return result
    
print(permutation("federal"))
