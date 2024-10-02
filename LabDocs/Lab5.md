# Functions Lab 5

### Python Formula Translation Practice

1. Convert each of the following into a Python expression and write the expression  in Python

    a.                     ab+c

    b.                    a-bc

    c.                     a(b+c)

    d.                    (a+b) / c

    e.                     0.5ab

    f.                      0.5c(a+b)

    g.                     a² + b²

    h.                     sqrt(a² + b²)

    i.                       b² - 4ac

    j.                       -b + sqrt(b²-4ac)  /  2a

    k.                                   -b - sqrt(b²-4ac)  /  2a

2. Write a Python program that will have parameter values of a, b, and c and functions for each of the following. 

    a. Create Python expressions for a – g from above, assign each of them to a variable. In this case we’re just practicing writing expressions, so use expA, expB, expC, etc. as variable names. For example, the first one would be
```
    a,b,c = 6,5,-6

    expA = a * b + c
    expB = …
```
  Create a print statement so that if a = 6, b = 5, and c = -6, then the output would be
```
    6 * 5 + -6 = 24
```
I would write one expression at a time and then test it before moving on to the next.  If you don’t, you may have many errors to correct.

3. Turn each of h – k into a Python function. Name the functions pythag, discriminant, quadPlus, and quadMinus respectively. 

    a. Functions quadPlus and quadMinus must call/invoke discriminant (Yes, you will be invoking one function from within another function). Hint: The square root of a number can also be found by raising the number to the 0.5 power. For example, for item h, the function would be
```
def pythag(a, b):

   return (a**2 + b**2)**0.5
```
Write one function at time checking each function as you go (calling the function once each, using the a, b, and c variables.)


[Back to labs](../README.md)