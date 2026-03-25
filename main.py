
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
"a*y*u*i*o*"
  1 3 5 7 9
 0123456789
 
 * BONUS -- try using all
'''

'''
3
Write a function that generates random integers between 0 and 10 (inclusive) 
until the  sum becomes greater than 42
The program must print how many numbers were generated
(print the random generated numbers [for debug])

def count_draws_until_sum_exceeds(limit: int = 42) -> int:
  pass

8 10 8 4 6 7 1 
43

answer: 7
'''