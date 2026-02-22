from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI(title="FastAPI Demo")


class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    email: str
    age: Optional[int] = Field(None, ge=0, le=150)


class UserResponse(BaseModel):
    id: int
    name: str
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
        "age": request.age,
        "created_at": datetime.now(),
        "email": request.email,
    }
    users_db[next_id] = user
    next_id += 1
    return user


# 依赖注入 — 类似 ASP.NET 的 DI
def get_current_user():
    return {"user_id": 1, "role": "admin"}


@app.get("/api/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return current_user


# 中间件 — 类似 ASP.NET Middleware
@app.middleware("http")
async def log_request(request, call_next):
    print(f"Request:{request.method} {request.url}")
    response = await call_next(request)
    print(f"Response:{response.status_code}")
    return response
