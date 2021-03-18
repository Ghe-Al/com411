def cross_bridge(n):
  for i in range(0,n):
    print("Crossed step.")
  if n>5:
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")
def run():
  cross_bridge(3)
  cross_bridge(6)