our_input = input("Please enter a string: ")
vowels = ["a","e","i","o","u"]
index_list = []
for i in our_input:
    if i in vowels:
        index_number = vowels.index(i)
        index_list.append(index_number)

if index_list == sorted(index_list) :
    print("Positive")
else:
    print("Negative")