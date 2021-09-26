

total = 0

#function to sum digits of a number
def digsum(number):
    number=str(number)
    sum=0

    for i in range(0,len(number)):
        digit = number[i]

        sum += int(digit)

    return(sum)

# loop function for all 3 digit integers
for n in range(100,999):

    # check if sum is 5
    if digsum(n) == 5:
        print(n, digsum(n))
        total += 1

    # if sum is not 5, check if sum of sum digits is 5 ex. 14, 23
    elif digsum(digsum(n)) == 5:
        print(n, digsum(n))
        total += 1


print(total)
