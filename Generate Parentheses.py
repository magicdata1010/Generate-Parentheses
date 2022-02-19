# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 22:14:01 2022

@author: 91838
"""
def balanced_parens(n):
    stack=[]
    res=[]
    def backtrack(o,c):
        if o==c==n:
            res.append(''.join(stack))
        if o<n:
            stack.append('(')
            backtrack(o+1,c)
            stack.pop()
        if c<o:
            stack.append(')')
            backtrack(o,c+1)
            stack.pop()
            
    # Your code here!
    backtrack(0,0)
    return res



