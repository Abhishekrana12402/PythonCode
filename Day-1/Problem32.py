# Ques Link:https://leetcode.com/problems/longest-valid-parentheses/description/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        Max=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    Max=max(Max,i-stack[-1])
        return Max
        
                

        