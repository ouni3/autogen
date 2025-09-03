# 使用官方 Python 镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有应用文件到工作目录
COPY . .

# 暴露应用运行的端口
EXPOSE 8001

# 设置容器启动时执行的命令
CMD ["uvicorn", "app_agent:app", "--host", "0.0.0.0", "--port", "8001"]
