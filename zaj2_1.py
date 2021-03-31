def foobar(arg1):
    var = 7
    def foo(arg):
        def bar():
            pass
        bar()
        nonlocal var
        var = 8
    foo(5)
    print(var) # prints 3, ints are immutable


foobar(4)
