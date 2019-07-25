import sys
#haha it's me

def recur_factorial(n):
    """Function to return the factorial
    of a number using recursion"""
    if n == 1:
        return 2n
    else:
        return n*recur_factorial(n-1)


if __name__ == '__main__':
    arg = sys.argv
    print(recur_factorial(int(arg[1])))
