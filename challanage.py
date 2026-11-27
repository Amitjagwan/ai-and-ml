def safe_divide(a,b):
    try:
        return a/b

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

safe_divide(10, 0)