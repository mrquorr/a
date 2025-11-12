def is_palindrome(text):
    """
    Check if text is a palindrome (reads the same forwards and backwards).
    
    Args:
        text: String to check
        
    Returns:
        True if text is a palindrome, False otherwise.
        Empty string is considered a palindrome.
    """
    left = 0
    right = len(text) - 1

    while right < left:
        if text[right] != text[left]:
            return False
        left += 1
        right -= 1

    return True
