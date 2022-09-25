
import random


mass = [random.randint(0, 10) for i in range(5)]
print(mass)

def uslovie(x):
  if x % 2 == 0:
    return True
  return False

print(list(filter(uslovie, mass)))