def sum_even_numbers(numbers):
    """Return sum of all even numbers in the list"""
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total