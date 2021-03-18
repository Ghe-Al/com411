def display_ladder(step):
  for i in range(0,step):
    print("| |")
    print("***")
  if step>0:
    print("| |")
def create_ladder():
  print("How many steps remain?")
  display_ladder(int(input()))
def run():
  create_ladder()