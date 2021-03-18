def run():
  print("What strange markings do you see?")
  a=input()
  print("\nIdentifying...")
  for i in range (0,len(a),1):
    print("index {}: {}".format(i,a[i]))
  print("Done!")
run()