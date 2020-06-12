
def outer_func(msg):
    message = msg 

    def inner_function():
        print(message)

    return inner_function


hi_func = outer_func('Hi')
by_func = outer_func('Bye')

hi_func()
by_func()
