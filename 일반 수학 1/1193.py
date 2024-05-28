N = int(input())
number = 1
count = 1

while number <= N:
    number += count
    count +=1


if (count-1) %2 == 0:
    print(str(N-number+count)+'/'+str(number-N))
else:
    print(str(number-N)+'/'+str(N-number+count))
