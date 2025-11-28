# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> This is an example function
    that demonstrates the use of documentation strings in Python.

    Parameters:
    arg1: The first argument.
    arg2: The second argument (optional).S
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
