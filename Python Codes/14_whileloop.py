"""
As the name suggests, while loops execute statements while the condition is True. 
As soon as the condition becomes False, the interpreter comes out of the while loop.
"""

count = 5
while (count > 0):
  print(count)
  count = count - 1


"""
Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or 
decrement the counter variable (the variable count, in our case) or the loop will continue forever.
"""

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')