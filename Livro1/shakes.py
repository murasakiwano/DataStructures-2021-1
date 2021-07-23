import random

def generateOne(strlen):
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  res = ""
  for i in range(strlen):
    res = res + alphabet[random.randrange(27)]

  return res


def score(goal, teststring):
  numSame = 0
  for i in range(len(goal)):
    if goal[i] == teststring[i]:
      numSame = numSame + 1
  return numSame / len(goal)

def main():

  goalString = 'batatinha'.lower()
  newString = generateOne(len(goalString))
  bestScore = 0
  newScore = score(goalString, newString)
  bestString = ''
  i = 0

  while newScore < 0.9:
    if newScore > bestScore:
      bestString = newString
      bestScore = newScore

    i = i + 1
    if i == 1000000:
      i = 0
      print(bestScore, bestString)

    newString = generateOne(len(goalString))
    newScore = score(goalString, newString)
  
  print(newScore, newString)

main()