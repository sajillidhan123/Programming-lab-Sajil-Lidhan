myinput=input("Enter a word : ")
mylist =list(myinput) 
mylist = [ord(character) + 1 for character in mylist]
print(mylist)