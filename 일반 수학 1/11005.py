n, b = map(int, input().split())
index_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

arr = []
num = n

while(num >= b):


    arr.append((num%b))
    num //= b

arr.append((num))

for i in range(len(arr),0,-1):
    print(index_str[(arr[i-1])],end='')
