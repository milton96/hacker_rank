def average(array):
    items = set(array)
    return sum(items)/len(items)

if __name__ == '__main__':
    s = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    print(average(s))
