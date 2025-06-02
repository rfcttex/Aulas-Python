# Basic try-except
try:
  x = 1 / 0
except ZeroDivisionError:
  print("Division by zero!")

# try-except-else
try:
  x = 1 / 1
except ZeroDivisionError as erro:
  print(erro.__class__)
else:
  print("No exception occurred.")

# try-except-finally
try:
  x = 1 / 0
except ZeroDivisionError:
  print("Division by zero!")
finally:
  print("This always runs.")

# try-except-else-finally
try:
  x = 1 / 1
except ZeroDivisionError:
  print("Division by zero!")
else:
  print("No exception occurred.")
finally:
  print("This always runs.")

# Multiple excepts
try:
  x = int("a")
except ZeroDivisionError:
  print("Division by zero!")
except ValueError:
  print("Value error occurred!")