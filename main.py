print("Program Started!")
print("Please enter an ASCII code:")
n=int(input())
if n in range (32,127):
  print("The character represented by the ASCII code {} is: {}".format(n,chr(n)))
else:
  print("Error: invalid code introduced")
print("Please enter a standard character:")
n=str(input())
if len(n)==1:
  print("The ASCII code for {} is: {}".format(n,ord(n)))
  print("The next ASCII character is: {}".format(chr(ord(n)+1)))
else:
  print("Error: too many characters introduced")