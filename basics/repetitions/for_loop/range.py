def run():
  print("What level of brightness is required?")
  a=int(input())
  print("\nAdjusting brightness...")
  for i in range (2,a+1,2):
    print("Beep's brightness level: {}".format("*" * i))
    print("Bop's brightness level: {}".format("*" * i))