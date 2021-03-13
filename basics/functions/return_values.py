def sum_weights(e,o):
  return e+o
def calc_avg_weight(e,o):
  return sum_weights(e,o)/2
def run():
  print("What is the weight of Beep?")
  b1=int(input())
  print("What is the weight of Bop?")
  b2=int(input())
  print("What would you like to calculate? (sum or average)")
  n=str(input())
  if n=="sum":
    print(sum_weights(b1,b2))
  elif n=="average":
    print(calc_avg_weight(b1,b2))
  else:
    print("invalid input")
#run the program
run()