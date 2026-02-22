## Python 快速入门学习计划 — 写给 .NET 后端开发者

> **适用人群：** 有 C#/.NET 后端开发经验，希望快速掌握 Python 并进入 AI/Agent 开发领域
> **总预计时长：** 约 20 小时（建议 2-3 天集中学习）
> **环境：** Python 已安装 + PyCharm IDE

---

### 你的优势地图

作为 .NET 开发者，以下概念你已经掌握，学 Python 时只需做"翻译"：

| 你已经会的 (C#/.NET) | Python 中的对应 | 学习成本 |
|---|---|---|
| 类、继承、接口 | 类、继承、鸭子类型（Duck Typing） | 很低 |
| NuGet 包管理 | pip + venv 虚拟环境 | 很低 |
| async/await | async/await（几乎一样） | 很低 |
| LINQ | 列表推导式 + itertools | 中等 |
| ASP.NET Web API | FastAPI / Flask | 很低 |
| Entity Framework | SQLAlchemy | 低 |
| 强类型系统 | 动态类型 + Type Hints | 需要转变思维 |

这意味着你可以跳过大量"编程入门"内容，直接聚焦 Python 特有的东西。

---

### 第一阶段：Python 语法速通（约 4 小时）

**目标：** 能用 Python 流畅地写出你在 C# 中已经会写的逻辑。

#### 1.1 基础语法对照（1 小时）

在 PyCharm 中新建一个项目，创建 `learn_basics.py`，逐一练习以下内容：

**变量与类型** — Python 不需要声明类型，没有 `var` 关键字，直接写：

```python
# C#: string name = "Zhang San";
# Python:
name = "Zhang San"
age = 30
is_developer = True  # 注意：True/False 首字母大写
salary = 15000.50

# C# 的 var 推断 ≈ Python 的默认行为，但 Python 是真正的动态类型
# 同一个变量可以随时换类型（虽然不建议这么做）
```

**字符串操作** — Python 的 f-string 类似 C# 的字符串插值：

```python
# C#: $"Hello, {name}! You are {age} years old."
# Python:
greeting = f"Hello, {name}! You are {age} years old."

# 多行字符串（C# 的 @"..." 或 """ 原始字符串）
sql = """
    SELECT * FROM users
    WHERE age > 18
    ORDER BY name
"""

# 常用方法对照
text = "hello world"
text.upper()          # C#: text.ToUpper()
text.split(" ")       # C#: text.Split(" ")
text.replace("o", "0")  # C#: text.Replace("o", "0")
text.startswith("he")   # C#: text.StartsWith("he")
len(text)             # C#: text.Length  注意：Python 用函数而非属性
```

**集合类型** — 这是和 C# 差异较大的地方：

```python
# List（类似 C# 的 List<T>）
numbers = [1, 2, 3, 4, 5]
numbers.append(6)       # C#: numbers.Add(6)
numbers.insert(0, 0)    # C#: numbers.Insert(0, 0)
first = numbers[0]      # 一样
last = numbers[-1]      # Python 特色：负索引，取最后一个元素！
sub = numbers[1:3]      # 切片：取索引1到2的元素 [2, 3]

# Dict（类似 C# 的 Dictionary<TKey, TValue>）
user = {
    "name": "Zhang San",
    "age": 30,
    "skills": ["C#", "Python"]
}
user["email"] = "zs@test.com"   # 添加/修改
name = user.get("name", "未知")  # 安全取值，类似 TryGetValue

# Tuple（类似 C# 的元组，但更常用）
point = (10, 20)
x, y = point  # 解构赋值，C# 也有类似语法

# Set（类似 C# 的 HashSet<T>）
tags = {"python", "ai", "backend"}
```

**控制流** — 几乎一样，但注意缩进代替花括号：

```python
# if/elif/else（C# 的 else if 在 Python 中是 elif）
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# for 循环（Python 没有 C 风格的 for(i=0; i<n; i++)）
for item in numbers:
    print(item)

for i in range(10):        # range(10) ≈ Enumerable.Range(0, 10)
    print(i)

for i, item in enumerate(numbers):  # 同时拿索引和值
    print(f"Index {i}: {item}")

# while 循环 — 和 C# 基本一样
count = 0
while count < 5:
    print(count)
    count += 1  # Python 没有 count++ 语法
```

#### 1.2 函数与模块（1 小时）

```python
# 基本函数
def greet(name: str, greeting: str = "Hello") -> str:
    """这是文档字符串（docstring），类似 C# 的 XML 注释"""
    return f"{greeting}, {name}!"

# Type Hints — Python 3.5+ 支持类型注解（不强制，但强烈建议写）
# 对 C# 开发者来说会很亲切
def calculate_total(prices: list[float], tax_rate: float = 0.1) -> float:
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)

# *args 和 **kwargs — C# 中的 params 的升级版
def log(*args, **kwargs):
    # args 是位置参数的元组
    # kwargs 是关键字参数的字典
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

log(1, 2, 3, name="test", level="info")
# Args: (1, 2, 3)
# Kwargs: {'name': 'test', 'level': 'info'}

# Lambda — 类似 C# 的箭头函数，但只能写一行
square = lambda x: x ** 2  # C#: x => x * x
```

**模块与包：**

```python
# 导入模块 — 类似 C# 的 using
import os                        # C#: using System.IO;
import json                      # C#: using System.Text.Json;
from datetime import datetime    # C#: using static System.DateTime;
from pathlib import Path         # C#: using System.IO.Path;

# 安装第三方包（在 PyCharm Terminal 中执行）
# pip install requests           类似 NuGet: Install-Package HttpClient
# pip install fastapi             类似 NuGet: Install-Package ASP.NET
```

#### 1.3 Python 独有的核心特性（2 小时）

这部分是你需要重点花时间的，因为 C# 中没有直接对应物。

**列表推导式（List Comprehension）** — Python 的灵魂特性之一：

```python
# C#: var evens = numbers.Where(n => n % 2 == 0).ToList();
evens = [n for n in numbers if n % 2 == 0]

# C#: var squares = numbers.Select(n => n * n).ToList();
squares = [n * n for n in numbers]

# C#: var dict = items.ToDictionary(i => i.Id, i => i.Name);
user_names = {u["id"]: u["name"] for u in users}

# 嵌套推导（慎用，可读性会变差）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]  # [1,2,3,4,5,6,7,8,9]
```

**上下文管理器（with 语句）** — 类似 C# 的 `using` 语句：

```python
# C#: using var stream = new FileStream("data.txt", FileMode.Open);
# Python:
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 文件会自动关闭，和 C# 的 using 一样

# 也可以用于数据库连接、锁等任何需要清理的资源
```

**装饰器（Decorator）** — 类似 C# 的 Attribute，但更强大：

```python
import time
from functools import wraps

# 定义一个装饰器（类似 C# 的 [Attribute]）
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper

# 使用装饰器
@timer  # 类似 C# 的 [Timer] 标注
def slow_function():
    time.sleep(1)
    return "done"

# 你以后会大量看到装饰器，比如：
# @app.get("/api/users")     FastAPI 路由
# @property                   属性
# @staticmethod               静态方法
# @abstractmethod              抽象方法
```

**生成器（Generator）** — 类似 C# 的 `IEnumerable` + `yield return`：

```python
# C# 的 yield return 在 Python 中就是 yield
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 惰性求值，和 C# 的 LINQ 一样不会一次性算完
for num in fibonacci(10):
    print(num)
```

**异常处理** — 几乎和 C# 一样：

```python
# C#: try { } catch (Exception ex) { } finally { }
try:
    result = 10 / 0
except ZeroDivisionError as e:  # C#: catch (DivideByZeroException e)
    print(f"Error: {e}")
except Exception as e:          # C#: catch (Exception e)
    print(f"Unexpected: {e}")
finally:
    print("Cleanup")

# 自定义异常
class BusinessError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        super().__init__(message)
```

---

### 第二阶段：Python 面向对象与工程实践（约 4 小时）

**目标：** 用 Python 的方式写出工程级代码。

#### 2.1 面向对象编程（1.5 小时）

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

# 基本类 — 和 C# 类似，但更简洁
class Animal:
    def __init__(self, name: str, age: int):  # 构造函数 __init__
        self.name = name      # 没有 private/public，默认公开
        self._age = age        # 约定：单下划线开头表示 protected
        self.__secret = "x"    # 双下划线开头表示 name mangling（类似 private）

    @property                  # C# 的 get 属性
    def age(self) -> int:
        return self._age

    @age.setter                # C# 的 set 属性
    def age(self, value: int):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def speak(self) -> str:    # 普通方法
        return f"{self.name} says something"

    def __str__(self) -> str:  # C#: override string ToString()
        return f"Animal({self.name}, {self._age})"

    def __repr__(self) -> str: # C#: 调试时显示的信息
        return f"Animal(name='{self.name}', age={self._age})"


# 继承 — 和 C# 类似
class Dog(Animal):  # C#: class Dog : Animal
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)  # C#: base(name, age)
        self.breed = breed

    def speak(self) -> str:  # 重写（Python 不需要 override 关键字）
        return f"{self.name} says Woof!"


# 抽象类 — 类似 C# 的 abstract class
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


# dataclass — 类似 C# 的 record，非常好用
@dataclass
class User:
    name: str
    email: str
    age: int = 0
    tags: list[str] = field(default_factory=list)

    # 自动生成 __init__, __repr__, __eq__ 等
    # C# record 的 Python 版本

user = User(name="Zhang San", email="zs@test.com", age=30)
print(user)  # User(name='Zhang San', email='zs@test.com', age=30, tags=[])
```

#### 2.2 虚拟环境与项目结构（1 小时）

```bash
# 创建虚拟环境（类似 .NET 项目的隔离依赖）
python -m venv .venv

# 激活虚拟环境
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# PyCharm 通常会自动检测并提示你配置虚拟环境

# 安装依赖
pip install requests fastapi uvicorn

# 导出依赖清单（类似 packages.config 或 .csproj 的 PackageReference）
pip freeze > requirements.txt

# 从清单安装依赖（类似 dotnet restore）
pip install -r requirements.txt
```

**推荐的项目结构：**

```
my_project/
├── .venv/                  # 虚拟环境（不提交到 Git）
├── src/
│   ├── __init__.py         # 标记为 Python 包（类似命名空间）
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   └── api/
│       ├── __init__.py
│       └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_user_service.py
├── requirements.txt        # 类似 .csproj 的依赖声明
├── .gitignore
└── README.md
```

#### 2.3 异步编程（1 小时）

你在 C# 中已经熟悉 async/await，Python 的几乎一样：

```python
import asyncio
import httpx  # pip install httpx（类似 C# 的 HttpClient）

# C#: public async Task<string> FetchDataAsync(string url)
async def fetch_data(url: str) -> str:
    async with httpx.AsyncClient() as client:  # 类似 using var client = new HttpClient()
        response = await client.get(url)
        return response.text

# 并发执行多个异步任务
# C#: await Task.WhenAll(task1, task2, task3);
async def fetch_all():
    urls = [
        "https://api.github.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/todos/1"
    ]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)  # 类似 Task.WhenAll
    return results

# 运行异步代码
asyncio.run(fetch_all())
```

#### 2.4 单元测试（0.5 小时）

```python
# tests/test_calculator.py
import pytest  # pip install pytest（类似 NUnit/xUnit）

def add(a, b):
    return a + b

# 测试函数 — 以 test_ 开头即可，不需要 [Test] 标注
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

# 参数化测试 — 类似 [TestCase] 或 [InlineData]
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected

# 运行测试：在 Terminal 执行 pytest
# 或在 PyCharm 中右键 → Run 'pytest'
```

---

### 第三阶段：用 FastAPI 写一个后端项目（约 4 小时）

**目标：** 用你熟悉的 Web API 模式，快速建立 Python 后端开发的手感。

#### 3.1 FastAPI 入门（2 小时）

FastAPI 是 Python 界最接近 ASP.NET Web API 的框架，你会感到非常亲切。

```bash
pip install fastapi uvicorn pydantic
```

```python
# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI(title="My First Python API")

# Pydantic Model — 类似 C# 的 DTO / Request Model
class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    age: Optional[int] = Field(None, ge=0, le=150)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int]
    created_at: datetime

# 模拟数据库
users_db: dict[int, dict] = {}
next_id = 1

# GET — 类似 [HttpGet("api/users")]
@app.get("/api/users", response_model=list[UserResponse])
async def get_users():
    return list(users_db.values())

# GET by ID — 类似 [HttpGet("api/users/{id}")]
@app.get("/api/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# POST — 类似 [HttpPost("api/users")]
@app.post("/api/users", response_model=UserResponse, status_code=201)
async def create_user(request: CreateUserRequest):
    global next_id
    user = {
        "id": next_id,
        "name": request.name,
        "email": request.email,
        "age": request.age,
        "created_at": datetime.now()
    }
    users_db[next_id] = user
    next_id += 1
    return user

# 依赖注入 — 类似 ASP.NET 的 DI
def get_current_user():
    # 实际项目中这里会解析 JWT Token
    return {"user_id": 1, "role": "admin"}

@app.get("/api/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return current_user

# 中间件 — 类似 ASP.NET Middleware
@app.middleware("http")
async def log_requests(request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response: {response.status_code}")
    return response
```

启动服务：

```bash
uvicorn main:app --reload --port 8000
# 访问 http://localhost:8000/docs 可以看到自动生成的 Swagger UI（和 .NET 一样！）
```

#### 3.2 项目实战：搭建完整的 CRUD API（2 小时）

建议动手做一个完整的小项目，比如"待办事项 API"或"笔记管理 API"，包含：

1. **项目结构**：按上面推荐的目录结构组织代码
2. **数据模型**：用 Pydantic 定义请求/响应模型
3. **路由分组**：用 `APIRouter` 组织路由（类似 ASP.NET 的 Controller）
4. **异常处理**：全局异常处理器
5. **数据库**：用 SQLAlchemy + SQLite 做简单的数据持久化

```python
# 路由分组示例 — 类似 Controller 的分组
from fastapi import APIRouter

router = APIRouter(prefix="/api/todos", tags=["Todos"])

@router.get("/")
async def list_todos():
    pass

@router.post("/")
async def create_todo():
    pass

# 在 main.py 中注册
# app.include_router(router)  类似 .NET 的 app.MapControllers()
```

---

### 第四阶段：进入 AI/Agent 世界（约 6 小时）

**目标：** 掌握 AI 开发的核心工具链，能独立构建 AI Agent。

#### 4.1 Python 数据处理基础（1 小时）

AI 开发离不开数据处理，先快速熟悉两个核心库：

```bash
pip install pandas numpy
```

```python
import pandas as pd
import numpy as np

# Pandas — 处理结构化数据的利器
# 类似 C# 的 DataTable，但强大 100 倍
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85.5, 92.0, 78.5]
})

# 筛选 — 类似 LINQ 的 Where
adults = df[df["age"] >= 30]

# 排序 — 类似 LINQ 的 OrderBy
sorted_df = df.sort_values("score", ascending=False)

# 聚合 — 类似 LINQ 的 GroupBy + Aggregate
avg_score = df["score"].mean()

# 读写文件
df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")
```

#### 4.2 OpenAI SDK 与大模型调用（1.5 小时）

```bash
pip install openai
```

```python
from openai import OpenAI

# 初始化客户端
client = OpenAI(api_key="your-api-key")  # 或设置环境变量 OPENAI_API_KEY

# 基本对话
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "你是一个有用的助手"},
        {"role": "user", "content": "用 Python 写一个快速排序"}
    ]
)
print(response.choices[0].message.content)

# 流式输出
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "写一首关于编程的诗"}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

# Function Calling — AI Agent 的核心能力
import json

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名"},
                },
                "required": ["city"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "北京今天天气怎么样？"}],
    tools=tools
)

# 检查模型是否要求调用函数
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    print(f"AI 想调用: {function_name}({arguments})")
```

#### 4.3 LangChain 快速入门（2 小时）

LangChain 是当前最流行的 AI 应用框架：

```bash
pip install langchain langchain-openai langchain-community
```

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

# 基本链（Chain）— AI 应用的核心构建模式
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}，请用{style}的风格回答问题"),
    ("human", "{question}")
])

# 用 LCEL（LangChain Expression Language）组装链
chain = prompt | llm | StrOutputParser()

result = chain.invoke({
    "role": "Python 导师",
    "style": "简洁明了",
    "question": "Python 和 C# 最大的区别是什么？"
})
print(result)
```

**RAG（检索增强生成）** — 让 AI 基于你的文档回答问题：

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# 1. 准备文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_text("你的长文档内容...")

# 2. 创建向量数据库
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)

# 3. 创建 RAG 链
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o"),
    retriever=vectorstore.as_retriever()
)

# 4. 提问
answer = qa_chain.invoke("根据文档，XXX 是什么意思？")
```

#### 4.4 构建你的第一个 AI Agent（1.5 小时）

```python
from langchain_openai import ChatOpenAI
from langchain.agents import tool, AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import requests

# 定义工具（Agent 可以使用的能力）
@tool
def search_web(query: str) -> str:
    """搜索网络获取实时信息"""
    # 实际开发中接入搜索 API
    return f"搜索 '{query}' 的结果：这是模拟的搜索结果..."

@tool
def calculate(expression: str) -> str:
    """计算数学表达式"""
    try:
        result = eval(expression)  # 生产环境建议使用安全的计算方式
        return str(result)
    except Exception as e:
        return f"计算错误: {e}"

@tool
def get_current_time() -> str:
    """获取当前时间"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 创建 Agent
llm = ChatOpenAI(model="gpt-4o", temperature=0)
tools = [search_web, calculate, get_current_time]

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的AI助手，可以使用工具来帮助用户。"),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 运行 Agent — 它会自己决定使用哪些工具
result = agent_executor.invoke({
    "input": "现在几点了？另外帮我算一下 (125 * 37 + 892) / 4.5"
})
print(result["output"])
```

---

### 第五阶段：进阶方向与持续学习（约 2 小时）

**目标：** 明确下一步学习路径。

#### 5.1 进阶内容速览（1 小时）

快速了解以下内容，根据实际需要深入学习：

**包管理进阶：** 了解 Poetry 或 uv（更现代的包管理工具，类比 .NET 从 packages.config 到 SDK-style .csproj 的演进）。

**类型系统：** 深入学习 typing 模块（Protocol、TypeVar、Generic），结合 mypy 做静态类型检查。这是让 Python 代码更接近 C# 严谨性的关键工具。

**异步框架：** 深入 asyncio，了解 Event Loop 机制。学习 aiohttp 或 httpx 的异步用法。

**数据库 ORM：** SQLAlchemy 2.0 的现代用法，特别是与 FastAPI 的配合。

**部署：** Docker 容器化部署 Python 应用，与你已有的 .NET Docker 经验相结合。

#### 5.2 推荐学习资源

**官方文档（最权威）：**
- Python 官方教程：https://docs.python.org/3/tutorial/
- FastAPI 官方教程：https://fastapi.tiangolo.com/tutorial/
- LangChain 文档：https://python.langchain.com/docs/

**适合 .NET 开发者的速查：**
- Python for C# Developers（搜索这个关键词会找到很多对照文章）
- Real Python（https://realpython.com）— 高质量教程网站

**AI/Agent 方向：**
- OpenAI Cookbook：https://cookbook.openai.com
- DeepLearning.AI 短课程：https://www.deeplearning.ai/short-courses/
- LangChain 官方教程和 YouTube 频道

**书籍推荐：**
- 《Fluent Python》（流畅的Python）— 进阶必读
- 《Python Cookbook》— 实用技巧大全

---

### 20 小时学习进度表

| 时间段 | 内容 | 预计耗时 | 产出 |
|---|---|---|---|
| Day 1 上午 | 第一阶段：语法速通 | 4h | 一个练习文件，覆盖所有基础语法 |
| Day 1 下午 | 第二阶段：OOP + 工程实践 | 4h | 一个规范的项目结构 + 测试 |
| Day 2 上午 | 第三阶段：FastAPI 实战 | 4h | 一个完整的 CRUD API |
| Day 2 下午 | 第四阶段：AI 基础 | 3h | OpenAI API 调用 + 数据处理 |
| Day 3 上午 | 第四阶段：Agent 开发 | 3h | 一个可运行的 AI Agent |
| Day 3 下午 | 第五阶段：进阶规划 | 2h | 明确后续学习路径 |

---

### 写给 .NET 开发者的 Python 备忘录

| 场景 | C# / .NET | Python |
|---|---|---|
| 包管理器 | NuGet | pip / Poetry / uv |
| 项目文件 | .csproj | requirements.txt / pyproject.toml |
| 依赖还原 | dotnet restore | pip install -r requirements.txt |
| 运行项目 | dotnet run | python main.py |
| 运行测试 | dotnet test | pytest |
| Web 框架 | ASP.NET Web API | FastAPI / Django / Flask |
| ORM | Entity Framework | SQLAlchemy / Django ORM |
| 序列化 | System.Text.Json | json / Pydantic |
| HTTP 客户端 | HttpClient | httpx / requests |
| 异步 | Task / async-await | asyncio / async-await |
| 依赖注入 | 内建 DI 容器 | FastAPI Depends / dependency-injector |
| Swagger | Swashbuckle | FastAPI 自带 |
| 日志 | ILogger / Serilog | logging / loguru |
| 配置 | appsettings.json | .env + python-dotenv |

---

> **最后一个建议：** 不要试图把 C# 的写法原封不动搬到 Python 里。Python 有自己的哲学——"There should be one obvious way to do it"。多读优秀的 Python 开源代码（比如 FastAPI 和 LangChain 的源码），感受 Pythonic 的写法，你会越来越喜欢这门语言的。
