def count_vowels(word):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
    # Use a generator expression to count non-'y' vowels in the word
    vowel_count = sum(1 for char in word if char in vowels and char.lower() != 'y')
    
    return vowel_count

# Example usage:
word_input = input("Enter a word: ")
result = count_vowels(word_input)
print(f'The number of non-"y" vowels in "{word_input}" is: {result}')
