name = "Zhang San"
age = 30
is_developer = True
salary = 15000.50

greeting = f"Hello,{name}! You are {age} years old."
print(greeting)

sql = """
    SELECT * FROM users
    WHERE age > 18
    ORDER BY name
"""

text = "Hello World"
text.upper()
text.split(" ")
text.replace("o", "O")
text.startswith("He")
len(text)

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, 0)
first = numbers[0]
last = numbers[-1]
sub = numbers[1:3]

user = {
    "name": "Zhang San",
    "age": 30,
    "skills": ["C#", "Python"]
}

user["email"] = "zs@test.com"
name = user.get("name", "未知")

point = (10, 20)
x, y = point

tags = {"Python", "ai", "backend"}

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

for item in numbers:
    print(item)

for i in range(10):
    print(i)

for i, item in enumerate(numbers):
    print(f"Index {i} :{item}")

count = 0
while count < 5:
    print(count)
    count += 1


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting} {name}!"


def calculate_total(prices: list[float], tax_rate: float = 0.1) -> float:
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)


def log(*args, **kwargs):
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")


log(1, 2, 3, name="test", level="info")

square = lambda x: x ** 2  # C# x=> x * x

import os
import json
from datetime import datetime
from pathlib import Path

# 安装第三方包（在PyCharm terminal 中执行）

evens = [n for n in numbers if n % 2 == 0]
# C# var evens = numbers.Where(n=>n%2==0).ToList();

squares = [n * n for n in numbers]
# C# var squares=numbers.Select(n=>n*n).ToList();

user_names = {u["id"]: u["name"] for u in user}
# C# var dict=items.ToDictionary)i=>i.Id,i=>i.Name);

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(1)
    return "done"


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(100):
    print(num)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Cleanup")


class BusinessError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        super().__init__(message)
