print("What is your name?")
n = input()
if len(n)>9:
  print("You have a realy long name!")
  print("Your name has {} letters".format(len(n)))
else:
  print("Your name is fine")
print("program end")