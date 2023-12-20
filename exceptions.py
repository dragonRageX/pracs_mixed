class BaseError(Exception): pass
class HighValueError(Exception): pass
class LowValueError(Exception): pass

value = 29
try:
    n = int(input("Enter number: "))
    if n < value:
        raise LowValueError
    elif n > value:
        raise HighValueError
except LowValueError:
    print("Very low value!")
except HighValueError:
    print("Very high value!")
else:
    print("Correct value!")
finally:
    print("Go")