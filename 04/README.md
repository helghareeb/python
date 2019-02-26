# بسم الله الرحمن الرحيم

[TOC]

# More Control Flow Tools

Besides the [`while`](https://docs.python.org/3.8/reference/compound_stmts.html#while) statement just introduced, Python knows the usual control flow statements known from other languages, with some twists.

## `if` Statements

- Perhaps the most well-known statement type is the `if`  statement.  For example

- ```python
  >>> x = int(input("Please enter an integer: "))
  Please enter an integer: 42
  >>> if x < 0:
  ...     x = 0
  ...     print('Negative changed to zero')
  ... elif x == 0:
  ...     print('Zero')
  ... elif x == 1:
  ...     print('Single')
  ... else:
  ...     print('More')
  ...
  More
  ```

- There can be zero or more [`elif`](https://docs.python.org/3.8/reference/compound_stmts.html#elif) parts, and the [`else`](https://docs.python.org/3.8/reference/compound_stmts.html#else) part is optional.  

- The keyword ‘`elif`’ is short for ‘else if’, and is useful to avoid excessive indentation.  

- An  `if` … `elif` … `elif` … sequence is a substitute for the `switch` or `case` statements found in other languages.

## `for` Statements

- The [`for`](https://docs.python.org/3.8/reference/compound_stmts.html#for) statement in Python differs a bit from what you may be used to in C or Pascal.  

- Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s `for` statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.  

- ```python
  >>> # Measure some strings:
  ... words = ['cat', 'window', 'defenestrate']
  >>> for w in words:
  ...     print(w, len(w))
  ...
  cat 3
  window 6
  defenestrate 12
  ```

- If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy.  

- Iterating over a sequence does not implicitly make a copy.  

- The slice notation makes this especially convenient:

- ```python
  >>> for w in words[:]:  # Loop over a slice copy of the entire list.
  ...     if len(w) > 6:
  ...         words.insert(0, w)
  ...
  >>> words
  ['defenestrate', 'cat', 'window', 'defenestrate']
  ```

- With `for w in words:`, the example would attempt to create an infinite list, inserting `defenestrate` over and over again.

## The [`range()`](https://docs.python.org/3.8/library/stdtypes.html#range) Function

- If you do need to iterate over a sequence of numbers, the built-in function [`range()`](https://docs.python.org/3.8/library/stdtypes.html#range) comes in handy.  

- It generates arithmetic progressions

- ```python
  >>> for i in range(5):
  ...     print(i)
  ...
  0
  1
  2
  3
  4
  ```

- The given end point is never part of the generated sequence; `range(10)` generates 10 values, the legal indices for items of a sequence of length 10. 

- It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):

- ```python
  range(5, 10)
     5, 6, 7, 8, 9
  
  range(0, 10, 3)
     0, 3, 6, 9
  
  range(-10, -100, -30)
    -10, -40, -70
  ```

- To iterate over the indices of a sequence, you can combine `range()` and `len()`as follows

- ```python
  >>> a = ['Mary', 'had', 'a', 'little', 'lamb']
  >>> for i in range(len(a)):
  ...     print(i, a[i])
  ...
  0 Mary
  1 had
  2 a
  3 little
  4 lamb
  ```

- In most such cases, however, it is convenient to use the [`enumerate()`](https://docs.python.org/3.8/library/functions.html#enumerate) function, see [Looping Techniques](https://docs.python.org/3.8/tutorial/datastructures.html#tut-loopidioms).

- A strange thing happens if you just print a range:

- ```python
  >>> print(range(10))
  range(0, 10)
  ```

- In many ways the object returned by [`range()`](https://docs.python.org/3.8/library/stdtypes.html#range) behaves as if it is a list, but in fact it isn’t. 

- It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

- We say such an object is *iterable*, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. 

- We have seen that the `for` statement is such an *iterator*. The function `list()` is another; it creates lists from iterables:

- ```python
  >>> list(range(5))
  [0, 1, 2, 3, 4]
  ```
## `break` and `continue` Statements, and `else` Clauses on Loops

- The [`break`](https://docs.python.org/3.8/reference/simple_stmts.html#break) statement, like in C, breaks out of the innermost enclosing [`for`](https://docs.python.org/3.8/reference/compound_stmts.html#for) or [`while`](https://docs.python.org/3.8/reference/compound_stmts.html#while) loop.

- Loop statements may have an `else` clause; it is executed when the loop terminates through exhaustion of the list (with [`for`](https://docs.python.org/3.8/reference/compound_stmts.html#for)) or when the condition becomes false (with [`while`](https://docs.python.org/3.8/reference/compound_stmts.html#while)), but not when the loop is terminated by a [`break`](https://docs.python.org/3.8/reference/simple_stmts.html#break) statement.  

- This is exemplified by the following loop, which searches for prime numbers

- ```python
  >>> for n in range(2, 10):
  ...     for x in range(2, n):
  ...         if n % x == 0:
  ...             print(n, 'equals', x, '*', n//x)
  ...             break
  ...     else:
  ...         # loop fell through without finding a factor
  ...         print(n, 'is a prime number')
  ...
  2 is a prime number
  3 is a prime number
  4 equals 2 * 2
  5 is a prime number
  6 equals 2 * 3
  7 is a prime number
  8 equals 2 * 4
  9 equals 3 * 3
  ```

- (Yes, this is the correct code.  Look closely: the `else` clause belongs to the [`for`](https://docs.python.org/3.8/reference/compound_stmts.html#for) loop, **not** the [`if`](https://docs.python.org/3.8/reference/compound_stmts.html#if) statement.)

- When used with a loop, the `else` clause has more in common with the `else` clause of a [`try`](https://docs.python.org/3.8/reference/compound_stmts.html#try) statement than it does that of [`if`](https://docs.python.org/3.8/reference/compound_stmts.html#if) statements: a `try` statement’s `else` clause runs when no exception occurs, and a loop’s `else` clause runs when no `break` occurs. 

- For more on the `try` statement and exceptions, see [Handling Exceptions](https://docs.python.org/3.8/tutorial/errors.html#tut-handling).

- The [`continue`](https://docs.python.org/3.8/reference/simple_stmts.html#continue) statement, also borrowed from C, continues with the next iteration of the loop:

- ```python
  >>> for num in range(2, 10):
  ...     if num % 2 == 0:
  ...         print("Found an even number", num)
  ...         continue
  ...     print("Found a number", num)
  Found an even number 2
  Found a number 3
  Found an even number 4
  Found a number 5
  Found an even number 6
  Found a number 7
  Found an even number 8
  Found a number 9
  ```

## `pass` Statements

- The pass statement does nothing. 

- It can be used when a statement is required syntactically but the program requires no action

- ```python
  >>> while True:
  ...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
  ...
  ```

- This is commonly used for creating minimal classes

- ```python
  >>> class MyEmptyClass:
  ...     pass
  ...
  ```

- Another place [`pass`](https://docs.python.org/3.8/reference/simple_stmts.html#pass) can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. 

- The `pass` is silently ignored

- ```python
  >>> def initlog(*args):
  ...     pass   # Remember to implement this!
  ...
  ```

- 