N = int(input())

value = 2
room = 1

while True:
    if N < value:
        break
    else:
        value = value + room*6
    room = room+1

print(room)