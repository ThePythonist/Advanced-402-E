def find_largest(*args):
    lst = []
    for i in args:
        lst.append(max(i))

    return lst

x1 = [10,20,40]
x2 = [60,50,70]
x3 = [110,120,60]

print(find_largest(x1,x2,x3))
