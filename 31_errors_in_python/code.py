def divide(dividend, divisor):
    if(divisor == 0):
        raise ZeroDivisionError("Divisor cannot be 0")
    return dividend/divisor


grades = [78, 99, 85, 100]

try:
    divide(2, 0)
except ZeroDivisionError as e:
    print(e)
    print('There are no grades yet in your list')


print(f"The average g")
