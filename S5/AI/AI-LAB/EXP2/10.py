def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, number):
    if (number % i) == 0:
      return False
  return True

num = int(input("Enter a number to check: "))

if is_prime(num):
  print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")
