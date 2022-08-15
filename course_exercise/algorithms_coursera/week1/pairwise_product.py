

n = int(input())
a = [int(x) for x in input().split()]

index1 = 0
for i in range(1, n):
    if a[i] > a[index1]:
        index1 = i
if index1 == 0:
    index2 = 1
else:
    index2 = 0
for j in range(1, n):
    if a[j] > a[index2] and j != index1:
        index2 = j

print(a[index1]*a[index2])