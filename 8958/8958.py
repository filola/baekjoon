def solution(ox):
  result = 0
  score = 1

  for i in ox:
    if i == "O":
      result += score
      score += 1
    else:
      score = 1

  return result

num = int(input())

for _ in range(num):
  print(solution(list(input())))


