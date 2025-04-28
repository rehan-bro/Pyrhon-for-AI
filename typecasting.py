name = "Rehan"
age = 24
cgpa = 3.62
is_student = True

# Typecasting
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>   
print(type(cgpa))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(str(age)))  # <class 'str'>
print(type(int(cgpa)))  # <class 'int'>
print(type(float(age)))  # <class 'float'>
print(type(bool(age)))  # <class 'bool'>
print(type(bool(cgpa)))  # <class 'bool'>
print(type(bool(name)))  # <class 'bool'>
print(type(bool(is_student)))  # <class 'bool'>
print(type(bool("")))  # <class 'bool'> (empty string is False)
print(type(bool(0)))  # <class 'bool'> (0 is False) 
print(type(bool(0.0)))  # <class 'bool'> (0.0 is False)
print(type(bool([])))  # <class 'bool'> (empty list is False)
print(type(bool({})))  # <class 'bool'> (empty dictionary is False)
print(type(bool(())))  # <class 'bool'> (empty tuple is False)
print(type(bool(None)))  # <class 'bool'> (None is False)
print(type(bool(True)))  # <class 'bool'> (True is True)
print(type(bool(False)))  # <class 'bool'> (False is False)
print(type(bool(1)))  # <class 'bool'> (1 is True)
print(type(bool(1.0)))  # <class 'bool'> (1.0 is True)
print(type(bool("Rehan")))  # <class 'bool'> (non-empty string is True)
print(type(bool([1, 2, 3])))  # <class 'bool'> (non-empty list is True)
print(type(bool({1: "a", 2: "b"})))  # <class 'bool'> (non-empty dictionary is True)
print(type(bool((1, 2, 3))))  # <class 'bool'> (non-empty tuple is True)
print(type(bool([0])))  # <class 'bool'> (non-empty list with 0 is True)
print(type(bool([0.0])))  # <class 'bool'> (non-empty list with 0.0 is True)
print(type(bool([None])))  # <class 'bool'> (non-empty list with None is True)
print(type(bool([False])))  # <class 'bool'> (non-empty list with False is True)
print(type(bool([True])))  # <class 'bool'> (non-empty list with True is True)
print(type(bool([1, 0])))  # <class 'bool'> (non-empty list with 1 and 0 is True)
print(type(bool([1.0, 0.0])))  # <class 'bool'> (non-empty list with 1.0 and 0.0 is True)
print(type(bool([1, 2, 3, 0])))  # <class 'bool'> (non-empty list with 1, 2, 3 and 0 is True)
print(type(bool([1, 2, 3, 0.0])))  # <class 'bool'> (non-empty list with 1, 2, 3 and 0.0 is True)
print(type(bool([1, 2, 3, None])))  # <class 'bool'> (non-empty list with 1, 2, 3 and None is True)
print(type(bool([1, 2, 3, False])))  # <class 'bool'> (non-empty list with 1, 2, 3 and False is True)
print(type(bool([1, 2, 3, True])))  # <class 'bool'> (non-empty list with 1, 2, 3 and True is True)
print(type(bool([1, 2, 3, "Rehan"])))  # <class 'bool'> (non-empty list with 1, 2, 3 and "Rehan" is True)
print(type(bool([1, 2, 3, ""])))  # <class 'bool'> (non-empty list with 1, 2, 3 and "" is True)