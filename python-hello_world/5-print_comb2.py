for num in range (100):
    if num < 99:
        print('{:02}, '.format(num), end="")
    else:
        print('{:02}\n'.format(num), end="")