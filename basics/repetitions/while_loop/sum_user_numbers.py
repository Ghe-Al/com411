def run():
  print("How many numbers should I sum up?")
  i=0
  s=0
  a=int(input())
  while(i<a):
    i=i+1
    print("Please enter number {} of {}".format(i,a))
    s=s+int(input())
  print("The answer is {}".format(s))