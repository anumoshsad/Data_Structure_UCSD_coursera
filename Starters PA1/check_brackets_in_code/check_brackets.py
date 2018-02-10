# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def f(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            bra = Bracket(next,i)
            opening_brackets_stack.append(bra)
        
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if not opening_brackets_stack:return i + 1
            top = opening_brackets_stack.pop()
            if not top.Match(next): return i+1
    if not opening_brackets_stack: return 'Success'
    else: return opening_brackets_stack[0].position + 1

if __name__ == "__main__":
    text = sys.stdin.read()
    print(f(text))

    # Printing answer, write your code here
