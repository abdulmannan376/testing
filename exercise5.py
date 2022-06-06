# Task: Make a filtered list of all the people who are over 18

"""
"age_over_18" function accepts "arr" as a paramter which is basically an array/lisy of key 
value pairs
First key => name, key => age
We need to perform following steps in this function:
1. We need to run the loop for each and every index of array (arr)
Note: each index of array contains both name and key value pair
2. We need to check if value if age(key) has greater than 18
3. If yes then we need to append it to a new array (we need to append whole index)
4. At the end we need to return it
"""

def age_over_18(arr):
  new_age = []
  for k in arr:
    if k['age'] > 18:
      new_age.append(k)
      # We are still inside the loop and 
      # once we got out of it then we need to return new_age as a whole array
      # return new_age.append(k)


  return new_age


# DO NOT EDIT CODE BELOW
# Test Cases:
print(age_over_18([
  { "name": "Peter Chan", "age": 22 },
  { "name": "Darren Chiu", "age": 12 },
  { "name": "Paul Lau", "age": 5 },
  { "name": "Erika Lee", "age": 30 },
  { "name": "Anthony Wong", "age": 16 } 
]))

# Expected Output: 
#[ { name: 'Peter Chan', age: 22 },
#  { name: 'Erika Lee', age: 30  }]