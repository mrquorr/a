def is_valid_parentheses(s):
    """
    Check if string has valid/balanced parentheses, brackets, and braces.
    
    Valid means:
    - Every opening bracket has a corresponding closing bracket
    - Brackets are closed in the correct order
    - No unmatched brackets
    
    Args:
        s: String containing only '(', ')', '{', '}', '[' and ']'
        
    Returns:
        True if parentheses are valid, False otherwise.
    """
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            if stack.pop() == matching[char]:
                return False

    return len(stack) == 0
