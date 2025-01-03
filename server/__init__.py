from fastapi import FastAPI
from contextlib import asynccontextmanager
from .models import init_db
from .routers import api_sound

# Lifespan 管理 FastAPI 的生命週期
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 啟動前的初始化邏輯
    print("初始化資料庫...")
    init_db()  # 初始化資料表

    yield  # 等待應用啟動完成

    # 關閉時的清理邏輯
    print("關閉應用：進行清理工作...")

# 創建 FastAPI 應用，並註冊 lifespan
app = FastAPI(lifespan=lifespan)

app.include_router(router= api_sound.router, prefix='/sound')