def run():
  print("Please enter a sequence")
  a=input()
  print("Please enter the character for the marker")
  b=input()
  s=1
  z=0
  for i in a:
    if i==b:
      for j in range(s,len(a),1):
        if a[j]==b:
          print("The distance between markers is: {}".format(z))
        z=z+1
    s=s+1
run()