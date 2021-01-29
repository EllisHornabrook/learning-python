# double prize money weekend bonanza
prizes = [15, 150, 250, 799, 1000]

double_prizes = []
for prize in prizes:
    double_prizes.append(prize*2)
print(double_prizes)

    # comprehension method
double_prizes = [ prize*2 for prize in prizes ]
        # does the same job but with less code
print(double_prizes)


# squaring numbers
nums = [3, 6, 39, 50, 191]

squared_even_nums = []
for num in nums:
    if (num ** 2) % 2 == 0:
        squared_even_nums.append(num ** 2)
print(squared_even_nums)

    # comprehension method
squared_even_nums = [ num ** 2 for num in nums if (num **2) % 2 == 0 ]
        # add what we want to list # cycle through # then apply conditions
print(squared_even_nums)