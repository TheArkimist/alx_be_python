size = int(input("Enter the size of the patter"))
counter = 1

while counter <= size:
  for col in range(size):
     print("*", end="") 
  print()

  counter+=1
