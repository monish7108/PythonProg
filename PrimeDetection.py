def is_prime(number):
    """Return True if *number* is prime."""
    if number==0:return False
    elif number==1:return False
    else:
        for element in range(2,number):
            if number % element == 0:
                return False
    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
            break

#number=int(input("Enter the number: "))
#print(is_prime(number))
#print("\n")
#print_next_prime(number)