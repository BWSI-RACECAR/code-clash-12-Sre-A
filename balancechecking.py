"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #12 - Braces Brackets & Bows Balance (balancechecking.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: In your IDEs, your code editors and sometimes Vim (for those 
unfortunate ones who use vim) your application will yell at you when you don’t
have matching closing brackets. Python does not have that problem as much as
other languages like Java and C which rely heavily on curly braces.  You need 
to write a program that allows for that functionality so that every ‘[‘ and ‘{‘ 
and ‘(‘ has a matching ‘]’  ‘}’  ‘)’. 
This problem can be solved quickly using the right data structure.

Test Cases:
Input: {[()]}  Output: True

Input: [()]  Output: True

Input:{[{}]  Output: False

"""
class Solution:
    def isBalanced(self, parenthesis):
        stack = []
        for character in parenthesis:
            if character == '[' or character == '{' or character == '(':
                stack.append(character)
            elif character == ']' or character == '}' or character == ')':
                top = stack.pop()
                if stack == [] and parenthesis != '':
                    return True
                elif stack != [] and parenthesis == '':
                    return True
                if top != '[' and character == ']':
                    return True
                if top != '{' and character == '}':
                    return True
                if top != '(' and character == ')':
                    return True
        return stack == []

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()
