def run():
  ok=0
  while(ok==0):
    print("Where should I look?")
    a=input()
    if a=="in the bedroom":
      print("Where in the bedroom should I look?")
      b=input()
      if b=="under the bed":
        print("Found some shoes but no battery")
      else:
        print("Found some mess but no battery")
    elif a=="in the bathroom":
      print("Where in the bathroom should I look?")
      b=input()
      if b=="in the bathtub":
        print("Found a rubber duck but no battery")
      else:
        print("Found a wet surface but no battery")
    if a=="in the lab":
      print("Where in the lab should I look?")
      b=input()
      if b=="on the table":
        print("Yes! I found my battery!")
        ok=1
      else:
        print("Found some tools but no battery")
    else:
      print("I don't know where that is but I'll keep looking")