import sys
input = sys.stdin.readline

suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])

