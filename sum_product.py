# Single line version of sum_product from pythonian23/misc

sum_product = lambda num: max([((num//n)**(n-(num%n))) * (((num//n)+1)**(num%n)) for n in range(num, 0, -1)])


for test in range(1, 20):
    print(test, sum_product(test))
