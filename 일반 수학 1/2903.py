n = int(input())

count = 0
value= 2
while count<n:
    value += 2**count
    count +=1

print(value*value)