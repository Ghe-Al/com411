def run():
  print("What phrase do you see?")
  a=input()
  print("\nReversing...\n")
  print("The phrase is: ", end="")
  for i in range (len(a),0,-1):
    print("{}".format(a[i-1]), end="")
  print("\n")
run()
  