# 0x00. Python - Variable Annotations

This repository contains examples and explanations related to Python variable annotations. Variable annotations in Python 3 allow developers to provide hints about the type of variables, enhancing code readability and enabling static analysis tools like mypy.

## Table of Contents

1. [Introduction](#introduction)
2. [Variable Annotations](#variable-annotations)
3. [Function Signatures](#function-signatures)
4. [Duck Typing](#duck-typing)
5. [Using Mypy for Validation](#using-mypy-for-validation)
6. [Examples](#examples)
7. [Contributing](#contributing)

## Introduction

Python is dynamically typed, meaning that variable types are determined at runtime. However, with the introduction of variable annotations, developers can add type hints to variables, function arguments, and return values. These annotations serve as documentation and can be used by static analysis tools to catch potential type-related errors.

## Variable Annotations

Variable annotations are added by using the colon (`:`) syntax to indicate the type of a variable.

```python

# Variable annotation example
age: int = 25
name: str = "John"
```

## Function Signatures

Function signatures can also be annotated, specifying the types of arguments and the return type.

```python

# Function signature annotation example
def add_numbers(a: int, b: int) -> int:
    return a + b
```

## Duck Typing

Python follows the philosophy of duck typing, where the type of an object is determined by its behavior rather than its explicit type. This allows flexibility in function arguments, promoting code reusability.

```python

# Duck typing example
def display_info(obj):
    print(obj.name)
    print(obj.age)
```

## Using Mypy for Validation

[Mypy](http://mypy-lang.org/) is a static type checker for Python that can be used to validate code based on variable annotations. To use mypy, install it using:

```bash
pip install mypy
```

Run mypy on your Python files to catch type-related errors early in the development process.

```bash
mypy your_file.py
```

## Examples

Explore the provided examples in this repository to see how variable annotations and mypy can be applied in real-world scenarios.

## Contributing

Feel free to contribute by adding more examples, improving documentation, or addressing any issues. Follow the [contribution guidelines](CONTRIBUTING.md) for a smooth collaboration process.
