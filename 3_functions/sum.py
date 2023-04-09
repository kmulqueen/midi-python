def return_sum(a, b):
    """ This is a function that returns the sum of two numbers """
    if isinstance(a, int) and isinstance(b, int):
        sum = a + b
        return sum


sum = return_sum(2, 8)
print(sum)