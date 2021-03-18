def run():
  print("What type of adventure should I have?")
  a=input()
  if a=="safe" or a=="long":
    print("Taking the safe route!")
  elif a=="scary" or a=="short":
    print("Entering the dark forest!")
  else:
    print("Not sure which route to take.")