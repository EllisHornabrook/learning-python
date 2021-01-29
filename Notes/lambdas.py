# small anon function that is only used once
nums = [1, 2, 3, 7, 9, 11]

    # using a function
def square(n):
    return n * n

print(list(map(square, nums)))


    # instead of calling a function, call lambda inline
print(list(map(lambda n: n * n, nums)))