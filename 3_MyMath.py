class MyMath:

    # single method to perform different operations
    def calculate(self, operation, n):

        # 1. Sum of first n natural numbers
        if operation == "sum":
            total = 0
            for i in range(1, n + 1):
                total += i
            print("Sum of first", n, "natural numbers =", total)

        # 2. First n prime numbers
        elif operation == "prime":
            print("First", n, "prime numbers are:")
            count = 0
            num = 2

            while count < n:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break

                if is_prime:
                    print(num, end=" ")
                    count += 1

                num += 1
            print()

        # 3. Fibonacci series
        elif operation == "fibonacci":
            print("Fibonacci series for", n, "numbers:")
            a = 0
            b = 1

            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()

        # 4. Factorial of a number
        elif operation == "factorial":
            fact = 1
            for i in range(1, n + 1):
                fact = fact * i
            print("Factorial of", n, "=", fact)

        else:
            print("Invalid operation selected")


# Create object
math_tool = MyMath()

# Menu for user
print("Mathematical Utility Tool")
print("1. Sum of first n natural numbers")
print("2. Display first n prime numbers")
print("3. Generate Fibonacci series")
print("4. Calculate factorial")

# Take input
choice = int(input("Enter your choice (1-4): "))
n = int(input("Enter the value of n: "))

# Perform selected operation
if choice == 1:
    math_tool.calculate("sum", n)

elif choice == 2:
    math_tool.calculate("prime", n)

elif choice == 3:
    math_tool.calculate("fibonacci", n)

elif choice == 4:
    math_tool.calculate("factorial", n)

else:
    print("Invalid choice")
