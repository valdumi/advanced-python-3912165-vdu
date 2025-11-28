# Example file for Advanced Python by Joe Marini
# Understanding Python scope


# declare a variable within the global scope
x = 1

# define a local function with a variable "x"
# def testfunc():
#     global x
#     x = 10
#     print("x inside function:", x)

# Run the test function and observe the two results
# testfunc()
# print("x outside function:", x)

# x = x + 5
# print("x after modification:", x)
# testfunc()

# Nested functions create inner scopes. These are called closures:
def multiplierMaker(factor):
  def multiply(number):
    return number * factor
  return multiply

doubler = multiplierMaker(2)
tripler = multiplierMaker(3)

print(doubler(10))
print(doubler(15))
print(tripler(10))
print(tripler(15))


