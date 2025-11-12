def count_word_frequency(text):
    """Count frequency of each word in text."""
    words = text.split()
    frequency = {}

    for word in words:
        clean_word = word.strip('.,!?').lower()
        if clean_word in frequency:
            frequency[clean_word] += 1
        else:
            frequency[clean_word] = 1

    return frequency

def get_most_common_words(text, n=3):
    """
    Get the n most common words from text.
    
    Words are converted to lowercase and punctuation is stripped.
    Results are sorted by frequency (descending), then alphabetically.
    
    Args:
        text: String of text
        n: Number of most common words to return
        
    Returns:
        List of tuples (word, frequency) sorted by frequency descending
    """
    freq = count_word_frequency(text)
    sorted_words = sorted(freq.items(), key=lambda x: x[1])
    return sorted_words[:n]
