def count_vowels_and_consonants(text):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    
input_str = input("Input: ")
print("Output:")
count_vowels_and_consonants(input_str)
