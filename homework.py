def h1(a):
  b=1
  for i in a:
    b=b*i
  print(b)

def h2(a):
  min=a[0]
  for i in a:
    if min>i:
      min=i
  print(min)

def h3(a):
  max=a[0]
  for i in a:
    if max<i:
      max=i
  print(max)

q=[1,5,5,8,2]
print("Select homework by number:")
print("1) Product of all elements")
print("2) Min element from an array")
print("3) Max element from an array")
n=int(input())
if n==1:
  h1(q)
if n==2:
  h2(q)
if n==3:
  h3(q)