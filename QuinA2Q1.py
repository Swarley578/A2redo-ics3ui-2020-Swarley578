# code for Q1
# put in any positive whole number and a sum of all the multiples of 3 and 5 will print

# ask the user to type in any positive whole number by setting int input as num
num = (int(input("type in any positive number: ")))

sum = 0 # set the variable sum so that it equals 0
for i in range(num): # create a for loop and put num as the range

    # every number between 0 and the number that has been input will divide by 3 and 5

    # the number will be added to all other numbers whose remainder is 0
    if (i%2 == 0 or i%3 == 0):
        sum = sum+i
print (sum) # the sum of all the numbers who have a remainder of 0 will be printed