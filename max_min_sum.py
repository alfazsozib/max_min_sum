#!/bin/python3

def miniMaxSum(arr):
    d = sum(arr)
    print(d-(max(arr)),(d-(min(arr))))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
