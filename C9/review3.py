def test(func):
    def new_func(*args, **kwargs):
            print('start')
            result = func(*args, **kwargs)
            return result
    print('end')
    return new_func

@test
def greet():
    print("Hello python")

greet()