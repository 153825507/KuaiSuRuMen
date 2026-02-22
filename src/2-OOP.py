from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age
        self.__secret = "x"

    # C# 的 get 属性
    @property
    def age(self) -> int:
        return self._age

    # C# 的 set 属性
    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # 普通方法
    def speak(self) -> str:
        return f"{self.name} says something"

    # C# override string ToString()
    def __str__(self) -> str:
        return f"Animal({self.name}, {self.age})"


# 继承 - 和 C# 类似
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} says Woof!"


# 抽象类 - 类似 C# 的 abstract class
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


# dataclass - 类似 C# 的 record,非常好用
@dataclass
class User:
    name: str
    email: str
    age: int = 0
    tags: list[str] = field(default_factory=list)


user = User(name="Zhang San", email="zs@test.com", age=10)
print(user)

import asyncio
import httpx  # pip install httpx（类似 C# 的 HttpClient）


async def fetch_data(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


async def fetch_all():
    urls = [
        "https://api.github.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/todos/1"
    ]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results


asyncio.run(fetch_all())
