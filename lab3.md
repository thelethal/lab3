# Reflection for Lab 3

## Part A: Analysis

### function 1:


```python
def function1(value, number):                   # 1 (function call)
    if (number == 0):                           # 1
        return 1                                # 1
    elif (number == 1):                         # 1
        return value                            # 1
    else:                                       # 1
        return value * function1(value, number-1)  # number recursive calls + number multiplications
The function multiplies value with itself number times (i.e., computes value^number using basic recursion).
Time Complexity: O(n)
Explanation: Each recursive call reduces number by 1, performing one multiplication at each step until it reaches 0. This leads to n recursive calls, where n = number.
Space Complexity (recursive stack): O(n)
Explanation: Each recursive call is added to the stack until the base case is reached. So, the maximum depth of the call stack is n, where n = number.
```

### function 2:


```python
def recursive_function2(mystring, a, b):                 # 1
    if(a >= b):                                          # 1
        return True                                      # 1
    else:                                                # 1
        if(mystring[a] != mystring[b]):                  # 1
            return False                                 # 1
        else:                                            # 1
            return recursive_function2(mystring, a+1, b-1)  # ≈ n/2 recursive calls

def function2(mystring):                                 # 1
    return recursive_function2(mystring, 0, len(mystring)-1)  # 1

This function checks if a string is a palindrome by comparing characters from the start and end toward the center.
Time Complexity: O(n)
Explanation: In each recursive call, the function compares 2 characters (mystring[a] and mystring[b]) and moves inward. This continues until a >= b, which takes about n/2 steps for a string of length n, which is O(n).
Space Complexity (recursive stack): O(n)
Explanation: Each call waits for the next to return before it can return its value, so all calls are added to the call stack until the center is reached. This means O(n) space in the worst case.

```

### function 3 (optional):


```python
def function3(value, number):                         # 1
    if (number == 0):                                 # 1
        return 1                                      # 1
    elif (number == 1):                               # 1
        return value                                  # 1
    else:                                             # 1
        half = number // 2                            # 1
        result = function3(value, half)               # log₂(n) recursive calls
        if (number % 2 == 0):                         # 1
            return result * result                    # log multiplications
        else:                                         # 1
            return value * result * result            # log multiplications
This function uses exponentiation by squaring, which is much more efficient than the basic recursive power calculation in function1.
Time Complexity: O(log n)
Explanation: Each recursive call halves the input number. Halving the input repeatedly takes log₂(n) steps, which is O(log n) time. Multiplication is constant per level.
Space Complexity (recursive stack): O(log n)
Explanation: Since the input size is halved with each recursive call, the call stack only grows to log₂(n) depth, resulting in O(log n) space usage.

```

## Part C reflection

Answer the following questions

1. How I approach writing recursive functions:
Honestly, when I first started writing recursive functions, they felt pretty intimidating. What helped me was breaking the problem down into two parts: the base case and the recursive case. I always start by asking myself, “When should this function stop calling itself?” That’s my base case.
Then, I look at how I can reduce the problem little by little until it reaches that base case. I usually sketch out a simple example (like a small list or number) and try to see how the function would behave step by step. After that, I just write the code and test it with small inputs to make sure it doesn't go into infinite recursion.
2. How I analyze recursive functions:
Analyzing recursive functions is a bit different than loops because you have to think in terms of function calls stacking up instead of iterations. It takes some getting used to, especially figuring out what each call returns and how that result is used in the previous call.
That said, it’s similar to regular functions in the sense that you still look at how data moves through the function and how it transforms. You just have to pay closer attention to the “flow” of calls and returns.
In short, recursion makes more sense the more I use it. It’s kind of like solving a riddle—once you get the trick, it starts to feel natural.

