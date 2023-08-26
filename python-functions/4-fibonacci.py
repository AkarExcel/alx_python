#!/usr/bin/env python3
# fibonacci sequence

def fibonacci_sequence(n):
    a = []
    if(n>=1):
        a.append(0)
    if(n>1):
        a.append(1)  
    for i in range(2, n):
        a.append(a[i-1] + a[i-2])
    return a

