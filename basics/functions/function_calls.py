def box(w):
  print("{}".format("*" * (len(w)+2)))
  print("*{}*".format(w))
  print("{}".format("*" * (len(w)+2)))
def ucase(w):
  print("{}".format(w.upper()))
def lcase(w):
  print("{}".format(w.lower()))
def mirrored(w):
  print("{}".format(w[::-1]))
def repeat(w):
  print("How many times should the word be repeated?")
  j=int(input())
  for i in range(0,j):
    if i%2==0:
      ucase(w)
    elif i%2==1:
      lcase(w)
def run():
  print("Enter a word:")
  w=str(input())
  print("1) Display in a box")
  print("2) Display Lower-Case")
  print("3) Display Upper-Case")
  print("4) Display Mirrored")
  print("5) Display Repeat")
  n=int(input())
  if(n==1):
    box(w)
  elif(n==2):
    lcase(w)
  elif(n==3):
    ucase(w)
  elif(n==4):
    mirrored(w)
  elif(n==5):
    repeat(w)
run()