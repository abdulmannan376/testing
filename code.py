# Task: Make a filtered list of all the people who are over 18

"""
Logic behind this function:
"ageOver18" function accepts "arr" as a parameter which is 
basically an array/list of key value pairs
As you can see in the below print statement that name and age are our keys and its data 
are supposed to be the value.
So we need to perform following steps in "ageOver18" function 
1. We need to Run a loop for each and every index of arr (array)
    Note: each index of array contains both name and age key value pair
2. We need to check if value of age(key) has greater than 18 (value)
3. If yes then we need to append all those array indexes to a new array (final_result)
4. At the end we need to return that final_result array
"""

def ageOver18(arr):
  final_result = []
  for x in arr:
    if x["age"] > 18:
      final_result.append(x)
  
  return final_result




# DO NOT EDIT CODE BELOW
# Test Cases:
print(ageOver18([
  { "name": "Peter Chan", "age": 22 },
  { "name": "Darren Chiu", "age": 12 },
  { "name": "Paul Lau", "age": 5 },
  { "name": "Erika Lee", "age": 30 },
  { "name": "Anthony Wong", "age": 16 } 
]))

# Expected Output: 
#[ { name: 'Peter Chan', age: 22 },
#  { name: 'Erika Lee', age: 30  }]