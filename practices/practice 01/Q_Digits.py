t = int(input())  # Read the number of test cases

while t > 0:
    n = int(input())  # Read the number for the current test case
    
    # Calculate the number of digits in n
    num_digits = len(str(n))
    
    # Extract and print the digits in reverse order
    for _ in range(num_digits):
        digit = n % 10  # Get the last digit of n
        print(digit, end=' ')
        n //= 10  # Remove the last digit from n
    
    t -= 1  # Decrement the number of remaining test cases
    print()  # Print a newline to separate test cases


# t = int(input())  

# while t > 0:
#     n = int(input())  
#     digits = []
    
#     while n > 0:
#         digit = n % 10  
#         digits.append(digit)
#         n //= 10
    
#     # Print the digits in reverse order
#     for digit in reversed(digits):
#         print(digit, end=' ')
    
#     t -= 1  # Decrement the number of remaining test cases
