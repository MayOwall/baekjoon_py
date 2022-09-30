num = int(input())
scoreList = list(map(int, input().split()))
mymax = max(scoreList)
sum = sum(scoreList)

print(sum * 100 / mymax / num)
