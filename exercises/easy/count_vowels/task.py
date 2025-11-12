def count_vowels(text):
    """Return the count of vowels in text"""
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in "aeio":
            count += 1
    return count