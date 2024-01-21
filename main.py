def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    pass

if __name__ == "__main__":
    print("Please input the calculation you want: ")
    mode = input()
    print("Input the first number: ")
    a = input()
    print("Input the second number: ")
    b = input()
    if mode == "add":
        print(f"The sum of {a} and {b} is: {add(a, b)}")
    elif mode == "multiply":
        print(f"The multiplication of {a} and {b} is: {multiply(a, b)} ")