N = int(input())
num = 1
k = 2
for i in range(2,5000):
    num += i
    if N <= num:
        break
    k += 1
## 이게 아니었어

