# 使用 Python 3.12 slim 镜像作为基础
FROM python:3.12-slim-bullseye

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir chainlit

# 将用户本地 bin 目录添加到 PATH
ENV PATH="/root/.local/bin:${PATH}"

# 复制所有项目文件
COPY . .

# 暴露 Chainlit UI 的端口
EXPOSE 8001

# 默认命令（在 docker-compose 中会被覆盖）
CMD ["python", "run_host.py"]
