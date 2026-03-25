
'''
1
Write a function

def average_score(scores: list[int]) -> float:
  pass
that receives a list of exactly three integers (0–100)
and returns the average as a float

Example: average_score([80, 90, 70]) → 80.0

if got list not with 3 numbers then -> return None
Or:
  raise ValueError("Expected exactly three scores")
'''

def average_score(scores: list[int]) -> float:
  if len(scores) != 3:
      raise ValueError("Expected exactly three scores")

  avg = sum(scores) / 3
  return avg

print(average_score([80, 90, 70]))
# print(average_score([80, 90, 70, 100]))

'''
2
def star_odd(word: str) -> bool:
  pass
  
You are given a string 
Print "yes" if every element at an odd index (1, 3, 5, …, 23) equals "*"
Otherwise print "no"

 0123
  1 3
"1*2*"

'''