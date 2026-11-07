#DICTIONARIES

my_dictionary{}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])

word = input ("Please type in a word: ")
if word in my_dictionary:
    print("translation:", my_dictionary[word])
else:
    print("Word not found in dictionary. ")

results = {}
results["Mary"] = 4
results ["Alice"] = 5
results["Tiana"] = 2

print(results)

lists = {}
lists[5] = [1,2,3]
lists[42] = [5,4,5,4,5,]
lists[100] = [5,2,3]
print(lists)

my_dictoioary
word_list = ["banana","butter", "milk", "beer, Cheeseburger", "chocolate", "juice" "pot roast","carrots", "Tuna" ]