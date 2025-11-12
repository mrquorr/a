def word_break(s, word_dict):
    """
    Check if string can be segmented into space-separated words from dictionary.
    
    Args:
        s: String to check
        word_dict: List of words (dictionary)
        
    Returns:
        True if string can be segmented, False otherwise
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] or s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]