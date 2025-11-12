def count_vowels(text):
    """
    Return the count of vowels (a, e, i, o, u) in the given text.
    
    Args:
        text: String to count vowels in
        
    Returns:
        Integer count of vowels (case-insensitive)
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in "aeio":
            count += 1
    return count