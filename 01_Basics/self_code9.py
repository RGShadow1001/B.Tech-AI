total=0
x=1
def add(y):
    global total
    total+=y
while x!=0:
    x=int(input("Enter a number: "))
    add(x)
print(f"the total sum is {total}")