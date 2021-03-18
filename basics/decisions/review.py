def run():
  print("Badabing?")
  a=input()
  if a == "a":
    print("a and b?")
    a=input()
    b=input()
    if a=="a" and b=="b":
      print("AND operator used successfully")
    elif a=="a" or b=="b":
      print("OR operator used successfully")
  elif not a=="Badaboom":
    print("I ain't got nothing to say to ya")
  else:
    print("Them's the times. How about it?")
    b=input()
    if b=="it is what it is":
      print("They really shouldn't let the review be this freeform")
    elif b!="random nonsense":
      print("You're making too much sense for this program")
    else:
      print("I feel ya.")
run()