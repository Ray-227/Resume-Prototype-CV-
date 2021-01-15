def squirrel(n):
    if (n < 0):
        return 'Error: n < 0, please enter n > 0'
        
    factorial = 1;
    for i in range(n, 0, -1):
        factorial *= i
    return int( str(factorial)[0] )
