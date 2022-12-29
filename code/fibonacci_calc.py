#!/usr/bin/env python3.7

def fibonacci(possition):
    if possition == 0:
        return 0
    elif possition == 1:
        return 1
    
    return fibonacci(possition-2)+fibonacci(possition-1)
    
asked_poss=int(input("which possition of fibonacci you need? "))
print(fibonacci(asked_poss))