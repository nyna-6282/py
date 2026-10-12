while True:
    print("\n .....MENU.....")
    print("a. Find the frequency of a character in a string . ")
    print("b. Replace a character by another character in a string .")
    print("c. Remove the first occurence of a character from a string  .")
    print("d. Remove all the occurences of a character from a string . ")
    print("e. Exit..")

    choice=input("Enter your choice(a/b/c/d/e) : ").lower()
    
    if choice=='e':
        print("Exiting the programme..")
        break
    string = input("Enter a string : ").lower()
    if choice=='a':
        char=input("Enterthe character to find frequency : ")
        print("Frequency of ",char," is ",string.count(char))   
    elif choice=='b':
        old=input("Enter the character to be replaced : ")
        new=input("Enter the new character : ")
        print("The modified string is : ",string.replace(old,new))
    elif choice=='c':
        char=input("Enter the character to remove (First Occurence ): ")
        print("The modified string is : ",string.replace(char, '',1))
    elif choice=='d':
        char=input("Enter the character to remove (All Occurences ): ")
        print("The modified string is : ",string.replace(char, ''))
    else :
        print("Invalid Choice ! Please select a valid option..")
        
