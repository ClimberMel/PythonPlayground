
def area(length, width):
    return length * width

def factorial(n):
    if n <= 0:
        print(n, "is not valid input") 
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def volume(length, width, height):
    #NOTE: it does not matter in what order the user provides the 3 variables
    return length * width * height

#NOTE:  The code below is only run if you run this module directly.
#       if imported from another module, the code below will be ignored

if __name__ == '__main__':
    l, w, h, f = 5, 7, 2, 8
    print(f"The area of a 2D shape {l} X {w} is: {area(l, w)}")
    print(f"The volume of a 3D shape {l} X {w} X {h} is: {volume(l, w, h)}")
    print(f"The factorial of {f} is: {factorial(f)}")