def check_even_odd(number):
    if number%2==0:
        print(f"The number {number} is even")
    else:
        print(f"the number {number} is odd")

print("type 0 to stop th eprogram")
while True:
    user_input=int(input("Enter a number:"))

    if user_input==0:
        print("Stopping..........Goodbye")
        break
    check_even_odd(user_input)