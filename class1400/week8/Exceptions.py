print("Raising Exceptions")
num = 0
while num < 1 or num > 10:
  try:
    num = int(input("Enter a number between 1 and 10: "))
    if num < 1 or num > 10:
        raise Exception("Value must be between 1 and 10")

  except ValueError:
    print("You must enter a number")

  except Exception as e:
    print("Oops, the number must between 1 and 10")

  finally:
    print("Good value or bad value I still show up!")