for i in range(5000): ##Range 5000 acts as a generator here. It doesnt store the values in memory but rather generates the data as a stream
    pass

print("Done")

list_ = [i for i in range(1000)] ## list object
generator_ = (i for i in range(10)) ## generator object
print generator_

## You can iterate over a generator object.

for i in generator_:
    print i 
