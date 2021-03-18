def run():
  print("What type of cover does the book have?")
  a=input()
  if a=="soft":
    print("Is the book perfect bound?")
    b=input()
    if b=="yes":
      print("Soft, perfect bound books are very popular!")
    elif b=="no":
      print("Soft covers with coils or stitches are great for short books")
    else:
      print("Invalid input")
  elif a=="hard":
    print("Books with hard covers can be more expensive!")
  else:
    print("Invalid input")
run()