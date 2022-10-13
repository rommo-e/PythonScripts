def is_palindrome(input_string):
    # In first insatance we have to create two strings to compare them 
    new_string = ""
    reverse_string = ""

    # We should now go through every letter of the word to check is order 
    for letter in input_string.strip():
        # In terms for readability we need to add non blank letter or spaces so 
        new_string = new_string+letter.replace(" ", "")
        reverse_string = letter.replace(" ","")+reverse_string

    # Now the important part for comparing the strings 
    if new_string.lower() == reverse_string.lower():
        return True 
    return False

print(is_palindrome("Anita Lava La Tina"))


