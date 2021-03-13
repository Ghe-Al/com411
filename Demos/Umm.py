print("Please choose an option from the menu: \n1 - Nice message \n2 - Area of a rectangle \n3 - Area of a triangle \n4 - Times table")

option = int(input())

if option == 1:
  print("Today will be a good day!")
elif option == 2:
  print("Enter the length of the rectangle:")
  l=int(input())
  print("Enter the width of the rectangle:")
  w=int(input())
  area=w*l
  print("The area of this rectangle is {}".format(area))
elif option == 3:
  print("Enter the length of a base:")
  l=float(input())
  print("Enter the length of the corresponding height:")
  h=float(input())
  area = 0.5*l*h
  print("The area of the triangle is {}".format(area))
elif option == 4:
  print("What number would you like to see times table for?")
  n = int(input())
  for i in range(1,11,1):
    print("{}x{}={}".format(n,i,n*i))
else:
  print("Invalid choice")