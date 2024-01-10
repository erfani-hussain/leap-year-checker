# Leap year program
print("Welcome to the Leap Year program!")

# input
year = int(input("Which year do u want to check? "))

# Nested if statements
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is a leap year.")
    else:
      print(f"{year} is not a leap year.")
  else:
    print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")