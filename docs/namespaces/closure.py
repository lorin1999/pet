def func_with_closure():
    a = 1

    def inner_func():
        b = a + 1
        print b
    inner_func()

func_with_closure()
