def is_palindrome(text):
    cleaned_text = ""

    for character in text:
        if character.isalnum():
            cleaned_text += character.lower()

    return cleaned_text == cleaned_text[::-1]


if __name__ == "__main__":
    print("Test 1:", is_palindrome("Kayak"))
    print("Test 2:", is_palindrome("Engage le jeu que je le gagne"))
    print("Test 3:", is_palindrome("Esope reste ici et se repose"))
    print("Test 4:", is_palindrome("Python"))
