import sys

inputy = sys.stdin.read().splitlines()
k = int(inputy[0])
index = 1
outputy = []

def intersects(A, B):
    x = len(A)
    return x

for _ in range(k):
    line1 = []
    line2 = []
    n = int(inputy[index])
    index+=1

    for __ in range(n):
        line1.append(inputy[index])
        index+=1
    for __ in range(n):
        line2.append(inputy[index])
        index+=1

    outputy.append(intersects(line1, line2))

for _ in outputy:
    print(_)
    



