

while True:
    N = int(input())
    
    if N == -1:
        break

    list = []
    sum = 0
    for i in range(1,N):
        if N%i == 0:
            list.append(i)
            sum += i
    
    if sum == N:
        print(N, " = ", " + ".join(str(i) for i in list), sep="")
    else:
        print(str(N) + ' is NOT perfect.')
    
    