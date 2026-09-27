person_information = {}
number_of_lines = int(input())
for line in range(number_of_lines) :
    sentence = input()
    name = ''
    age = ''
    for word in sentence.split():
        if "@" in word and "|" in word:
            start = word.index("@") + 1
            end = word.index("|")
            name = word[start:end]

        if "#" in word and "*" in word:
            start = word.index("#") + 1
            end = word.index("*")
            age = word[start:end]

    person_information[name] = age

for name, age in person_information.items():
    print(f"{name} is {age} years old.")


