def calculate(number):
    if number <= 1:
        return number
    else:
        return calculate(number - 1)*number

