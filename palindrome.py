def palindrome():
    text = input("Enter the name: ")
    reversed_text = text[::-1] # slices/splits the text startng with the last letter

    if text == reversed_text:
        print("This is a palindrome.")
        print(text)
    else:
        print("This isn't a palindrome. Try again.")

palindrome()