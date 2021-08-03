# 
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
# Python 2 and PyPy 2

def print_full_name(first, last):
    print("Hello "+first+" "+last+"! You just delved into python.")
    # Write your code here

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)

#Python 3 and PyPy 3

def print_full_name(first, last):
    # Write your code here
    print("Hello "+first+" "+last+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
