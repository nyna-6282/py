def freq():
    sentence=input("Enter a sentence : ").lower()
    f={}
    for char in sentence:
        f[char]=f.get(char,0)+1
    print("Letter Frequencies : ")
    for letter,count in sorted(f.items()):
        print(letter," : ",count)
freq()
