pwd=input("Enter the password")
isgranted=pwd=="secret123"
if isgranted:
    isgranted=True
    print(f"Access granted {isgranted}")
else:
    print(f"Access denied {isgranted}")