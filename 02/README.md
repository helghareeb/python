# بسم الله الرحمن الرحيم

[TOC]

# Python Interpreter

## Invoking the Interpreter

- The Python interpreter is usually installed as  ```/usr/local/bin/python3.8```

```shell
python3.8
```

- Anaconda

## Interactive Mode

```shell
$ python3.8
Python 3.8 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

# Interpreter and its Environment

- By default, Python source files are treated as encoded in UTF-8.  

- In that encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments — although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow.  

- To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.

- To declare an encoding other than the default one, a special comment line should be added as the *first* line of the file.  The syntax is as follows:

- ```python
  # -*- coding: encoding -*-
  ```

- ```python
  # -*- coding: cp1252 -*-
  ```

- One exception to the *first line* rule is when the source code starts with a
   UNIX “shebang” line.  In this case, the encoding declaration should be added as the second line of the file.  For example:

- ```python
  #!/usr/bin/env python3
  # -*- coding: cp1252 -*-
  ```