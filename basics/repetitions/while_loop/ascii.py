def run():
  print("How many bars should be charged?")
  a=int(input())
  i=0
  while (i<a):
    i=i+1
    print("Charging: {}".format("█ " * i))
  print("The battery is fully charged.")
run()