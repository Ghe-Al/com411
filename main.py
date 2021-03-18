<<<<<<< HEAD
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
def run_block_a():
 print("Which program in 'Block A: Basics' do you wish to run?")
 response = input()
 if (response == "simple_message"):
  simple_message.run()
 elif (response == "multiline_message"):
  multiline_message.run()
def run():
 is_running = True
 while(is_running):
  print("What would you like to do?")
  print("[a] Run 'Block A: Basics' programs")
  print("[q] Quit")
  response = input()
  if (response == "a"):
    run_block_a()
  elif (response == "q"):
    break
  else:
    print("Invalid option! Please try again.")
run()
=======
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
>>>>>>> 4625806eeb043c06b3c9f44279e37066880973b8
