

def double(x):
    return x*2


sequence = [1, 3, 4, 5, 6]
# doubled = [x*2 for x in sequence]

doubled = map(lambda x: x*2, sequence)

print(list(doubled))
