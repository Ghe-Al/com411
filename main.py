print("Program Started!")
print("Please enter an ASCII code:")
n=int(input())
if n in range (32,127):
  print("The character represented by the ASCII code {} is: {}".format(n,chr(n)))
else:
  print("Error: invalid code introduced")