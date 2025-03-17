import random
x=int(input("Enter your number between 10 and 20:"))
a=random.randint(10,20)
while True: 
  if a!=x:
    print("Please enter your number again")
    x=int(input("Enter your number between 10 and 20:"))  
  else:
    print("Congratulations!")
    break   
