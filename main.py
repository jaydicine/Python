
#chance that any 2 people in a given group of people have the same birthday, assuming all birthdays are equal (which they aren't)
import random

birthdays = []
matches = 0
total = 10000
students = 23

for i in range(0,total):
    birthdays = []
    for j in range(0, students):
        tempday = random.randint(1, 365)
        if tempday in birthdays:
            birthdays.append(tempday)
            matches += 1
            #print(birthdays)
            break
        else:
            birthdays.append(tempday)

    #if len(birthdays) == 20 and birthdays.count(tempday) == 1:
        #print(birthdays,  "NO REPEAT")
        #print(i)
    #else:
        #pass


print(matches)
print(matches / total)


