def cough_decorator(func):

    def func_wrapper():
            # code before function
        print('*cough*')
        func()
            # code after function
        print('*cough*')

    return func_wrapper

    # place the decorator above the functions you want to use it on
@cough_decorator
def question():
    print('Excuse me...')

@cough_decorator
def answer():
    print("Sorry I didn't see you there")

question()
answer()