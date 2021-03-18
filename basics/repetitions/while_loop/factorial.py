def run():
  print("Please enter a number:")
  i=int(input())
  j=0
  s=1
  while(j<i):
    j=j+1
    s=s*j
  print("The factorial is {}".format(s))
run()