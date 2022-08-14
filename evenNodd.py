even=0
odd=0
number=int(input("Starting number of series: "))
number2=int(input("Ending number of series: "))
for value in range(number,number2 + 1):
    if value%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)