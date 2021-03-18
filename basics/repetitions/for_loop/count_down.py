def run():
  print("How far are we from the cave?")
  a=int(input())
  for i in range(a,0,-1):
    print("{} steps remaining".format(i))
  print("We have reached the cave!")
run()