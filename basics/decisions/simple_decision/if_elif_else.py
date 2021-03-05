print("Towards which direction should I paint (up, down, left or right)?:")
a=str(input())
if a == "up":
  print("I am painting in the upward direction!")
elif a == "right":
  print("I am painting in the rightward direction!")
elif a == "down":
  print("I am painting in the downward direction!")
elif a == "left":
  print("I am painting in the leftward direction!")
else:
  print("That's not a direction")
print("Painting complete!")