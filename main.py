# 1
nums = [5, 2, 9, 1, 7]
print(sorted(nums, key=lambda x: -x))


# 2
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        res = func(*args, **kwargs)
        print("End")
        return res
    return wrapper

@decorator
def hello():
    print("Hello")

hello()


# 3
class A:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value > 0:
            self._x = value

obj = A(5)
obj.x = 10
print(obj.x)


# 4
from itertools import permutations
print(list(permutations([1, 2, 3], 2)))


# 5
import json
data = '{"a": 10, "b": 20}'
d = json.loads(data)
d["c"] = 30
print(json.dumps(d))
