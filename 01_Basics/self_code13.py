def inp(y):
   try:
       num = int(y)
       print(f"you entered {y}")
   except:
       print("Invalid Input Enter a number only!")
inp(input("Enter a number: "))