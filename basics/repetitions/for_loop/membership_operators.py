def run():
  print("What phrase do you see?")
  a=input()
  print("\nReversing\n")
  print("The phrase is: ", end="")
  for i in reversed(a):
    print("{}".format(i), end="")
  print("\n")