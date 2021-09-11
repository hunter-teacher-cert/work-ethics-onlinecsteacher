def factorial(n):
  prod = 1;
  i = n; #set i equal to parameter

  #for loop iterates from n decrementing by 1 until it gets to 1
  for i in range(i,1,-1):
    prod = prod * i

  return prod #return factorial

def fib(n):
  if (n<2):
    return 1
  else:
    return fib(n-1) + fib(n-2)

print("Good News Everyone!")

#test out factorial function
print(f"1! = {factorial(1)}")
print(f"3! = {factorial(3)}")
print(f"5! = {factorial(5)}")

#test out fibonacci function
print(f"fib(1) = {fib(1)}")
print(f"fib(3) = {fib(3)}")
print(f"fib(5) = {fib(5)}")
