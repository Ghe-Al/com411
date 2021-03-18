def run():
  print("Enter the first number:")
  a=int(input())
  print("Enter the second number:")
  b=int(input())
  print("Enter the third number:")
  c=int(input())
  z=0
  x=0
  for i in a,b,c:
    if i%2==0:
      z=z+1
    else:
      x=x+1
  print("There were {} even numbers and {} odd numbers".format(z,x))