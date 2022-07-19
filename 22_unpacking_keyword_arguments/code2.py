from unicodedata import name


def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}:{value}")


details = {"name": "Bob", "age": 25}

print_nicely(name='bob', age=25)
