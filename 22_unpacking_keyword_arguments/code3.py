def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="bob", age=21)
