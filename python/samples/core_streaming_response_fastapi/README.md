# **AutoGen-Core 流式聊天 API 与 FastAPI**

本示例演示了如何使用 `autogen-core` 和 FastAPI 构建一个具有多轮对话历史的流式聊天 API。

## **功能说明**

本示例的核心功能是提供一个基于 FastAPI 的聊天 API，支持实时流式响应和多轮对话历史。

### **主要特性**

1.  **流式响应**:
    *   通过利用 FastAPI 的 `StreamingResponse`、`autogen-core` 的异步特性以及使用 `asyncio.Queue()` 创建的全局队列来管理数据流，实现 LLM 响应的实时流式传输，从而提供更快的用户感知响应时间。
2.  **多轮对话**:
    *   智能体 (`MyAgent`) 可以接收和处理包含多轮交互的聊天历史记录 (`ChatHistory`)，从而实现上下文感知的连续对话。

## **文件结构**

*   `app.py`: FastAPI 应用程序代码，包括 API 端点、智能体定义、运行时设置和流式传输逻辑。
*   `README.md`: (本文档) 项目介绍和使用说明。

## **安装**

首先，请确保您已安装 Python（建议 3.8 或更高版本）。然后，在您的项目目录中，通过 pip 安装必要的库：

```bash
pip install "fastapi" "uvicorn[standard]" "autogen-core" "autogen-ext[openai]"
```

## **配置**

在与本 README 文件相同的目录中创建一个名为 `model_config.yaml` 的新文件，以配置您的模型设置。可以参考 `model_config_template.yaml` 文件作为示例。

**注意**: 将 API 密钥直接硬编码在代码中仅适用于本地测试。对于生产环境，强烈建议使用环境变量或其他安全方法来管理密钥。

## **运行应用程序**

在包含 `app.py` 的目录中，运行以下命令以启动 FastAPI 应用程序：

```bash
uvicorn app:app --host 0.0.0.0 --port 8501 --reload
```

服务启动后，API 端点将位于 `http://<您的服务器IP>:8501/chat/completions`。

## **使用 API**

您可以通过向 `/chat/completions` 端点发送 POST 请求与智能体进行交互。请求正文必须为 JSON 格式，并包含一个 `messages` 字段，其值为一个列表，其中每个元素代表一轮对话。

**请求正文格式**:

```json
{
  "messages": [
    {"source": "user", "content": "你好！"},
    {"source": "assistant", "content": "你好！我能帮你什么？"},
    {"source": "user", "content": "介绍一下你自己。"}
  ]
}
```

**示例 (使用 curl)**:

```bash
curl -N -X POST http://localhost:8501/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "messages": [
    {"source": "user", "content": "你好，我是 Tory。"},
    {"source": "assistant", "content": "你好 Tory，很高兴认识你！"},
    {"source": "user", "content": "用我的名字打个招呼并介绍一下你自己。"}
  ]
}'
```

**示例 (使用 Python requests)**:

```python
import requests
import json
url = "http://localhost:8501/chat/completions"
data = {
    'stream': True,
    'messages': [
            {'source': 'user', 'content': "你好，我是 Tory。"},
            {'source': 'assistant', 'content':"你好 Tory，很高兴认识你！"},
            {'source': 'user', 'content': "用我的名字打个招呼并介绍一下你自己。"}
        ]
    }
headers = {'Content-Type': 'application/json'}
try:
    response = requests.post(url, json=data, headers=headers, stream=True)
    response.raise_for_status()
    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            print(json.loads(chunk)["content"], end='', flush=True)

except requests.exceptions.RequestException as e:
    print(f"错误: {e}")
except json.JSONDecodeError as e:
    print(f"JSON 解码错误: {e}")
```
