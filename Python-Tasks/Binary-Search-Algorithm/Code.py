import random
# Importing in-built random fuction

arr=[random.randrange(0,100) for i in range(100)]
# List comprehension to create a list of random numbers 0 to 100

# print(len(arr))
find=int(input("Enter the number: "))
# User input

key=int(len(arr)/2)
# Hashing the array

while True:
    if len(arr)==1 and arr[0]==find:
    # Checking if the number is found
        # print("the number was found")
        break
    if len(arr)==1 and arr[0]!=find:
    # Checking if the number is not found
        # print("the number was not found")
        break
    if find in arr[:key]:
    # Checking lower half of the array
        # print(arr)
        arr=arr[:key]
    else:
    # Checking upper half of the array
        # print(arr)
        arr=arr[key:]

    key=int(len(arr)/2)
    # halving the pointer