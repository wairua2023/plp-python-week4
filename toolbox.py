def double(number):
    return number * 2


result1 = double(7)
result2 = double(10)


def is_pass(score):
    return score >= 50
    # Return the result of comparing score to 50
  

def greet(name, greeting="Hello"):
    # Return the greeting, a comma, the name, and an exclamation mark
    return f"{greeting}, {name}!"


print(double(7))
print(double(10))
print(is_pass(80)) 
print(is_pass(20))
print(greet("Amina"))  
print(greet("Brian", "Welcome")) 