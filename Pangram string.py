list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
sentence = input("Type a Sentence") 

pangram = True
for i in list:
    if i not in sentence:
        pangram = False
        break
if pangram == True:
    print("This is a pangram string.")
else:
    print("This is not a pangram string.")

