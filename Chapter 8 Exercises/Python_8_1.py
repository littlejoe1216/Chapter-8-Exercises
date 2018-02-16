#Joe Gutierrez - 2/1/18 - Chapter 8 - Exercise 1
#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.



a = ['a', 'b', 'c', 'd', 'e']

def chop(a):
  del a[0:]
  del a[4:]
  return a[1:b-1]
  
print(a) 
print (chop)
