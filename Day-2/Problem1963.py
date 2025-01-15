# Ques Link:https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        unbalanced=0
        for i in range(len(s)):
            if s[i]=='[':
                stack.append(s[i])
            else:
                if stack  and s[i]==']' and stack[-1]=='[':
                    stack.pop()
                    # pop the perfectly balanced para 
                else:
                  unbalanced+=1  
                #   track the count of closing coming before the openenings
        return (unbalanced+1)//2
        # Half swap will be required because swaping one pair can make the other para balance