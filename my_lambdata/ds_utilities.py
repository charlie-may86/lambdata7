def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

'''
anything below this only runs when you run this package
if you import this package, the stuff below if __name__ == '__main__'
won't run
'''

if __name__ == '__main__':
    print(enlarge(5))