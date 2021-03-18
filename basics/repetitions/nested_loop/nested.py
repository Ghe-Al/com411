def run():
  print("How many rows should I have?")
  a=int(input())
  print("How many columns should I have?")
  b=int(input())
  print("\nHere I go:\n")
  for i in range (0,a,1):
    for j in range (0,b,1):
      print(":-)", end="")
    print()
  print("\nDone!")