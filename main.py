shift = int(input("Shift"))
word = input("word")
wordlist = list(word)
newlist = []

for letter in wordlist:
    newlist.append(chr(ord(letter) + shift))

print(newlist)

oglist = []

for newletter in newlist:
    oglist.append(chr(ord(newletter) - shift))

print(oglist)


# separate

fruits = ["banana", "apple", "pineapple"]
newcodes = []

for fruit in fruits:
    newcodes.append(ord(fruit) + 5)