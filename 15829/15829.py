num = int(input())
abc = list(input())

r = 1
answer = 0

for i in range(num):
  answer += ((ord(abc[i])-96) * r)
   
  r *= 31

print(answer % 1234567891)