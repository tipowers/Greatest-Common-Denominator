# This program will ask the user to input an index and the greatest common denominator will be displayed

# Define main function
# Get user inputs of 'm' and 'n' from the user
# Print the results by calling the gcd function
def main():   
    m = eval(input('\nEnter the first index: '))
    n = eval(input('\nEnter the second index: '))

    print('\nThe greatest common denominator of ' + str(m) + ' and ' + str(n) + ' is ' + str(gcd(m, n)))

# Define gcd function with m and n as parameters
# Write recursion statement that if m % n == 0 return the base case
# Else return to gcd n and m%n as parameters
def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

# Call main function
main()

