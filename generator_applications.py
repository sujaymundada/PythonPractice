input_list = [5,10,2,34,45,65,7,80]

def div_five(num):
    return not bool(num%5)


xyz = (i for i in input_list if div_five(i))

for i in xyz:
    print i
