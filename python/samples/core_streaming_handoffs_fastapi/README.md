# **AutoGen-Core 流式聊天与 FastAPI 多智能体交接**

本示例演示了如何使用 `autogen-core` 和 FastAPI 构建一个具有多智能体交接和持久化对话历史的流式聊天 API。有关交接模式的更多详细信息，请参阅 [AutoGen 文档](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/handoffs.html)。

灵感来源于 `@ToryPan` 的 Core API 流式传输示例。

## **功能说明**

本示例的核心功能是提供一个基于 FastAPI 的聊天 API，支持实时流式响应、智能体之间的无缝交接以及持久化的对话历史。

### **主要特性**

1.  **流式响应**:
    *   利用 FastAPI 的 `StreamingResponse`、`autogen-core` 的异步特性和 `asyncio.Queue` 来管理数据流，实现智能体响应的实时流式传输。
2.  **多智能体交接**:
    *   展示了一个系统，其中不同的智能体（如分类智能体、销售智能体、问题与维修智能体）处理对话的不同部分。
    *   智能体使用工具（`delegate_tools`）根据对话上下文在智能体之间转移对话。
3.  **持久化多轮对话**:
    *   智能体接收并处理对话历史，从而实现上下文感知的交互。
    *   历史记录按对话 ID 保存在 `chat_history` 目录中的 JSON 文件中，允许对话在不同会话之间恢复。
4.  **简单 Web UI**:
    *   包含一个基本的 Web 界面（通过 FastAPI 的静态文件提供），方便直接从浏览器与聊天系统进行交互。

## **文件结构**

*   `app.py`: 主要的 FastAPI 应用程序代码，包括 API 端点、智能体定义、运行时设置、交接逻辑和流式传输。
*   `agent_user.py`: 定义负责与人类用户交互并保存聊天历史的 `UserAgent`。
*   `agent_base.py`: 定义专业智能体使用的基础 `AIAgent` 类。
*   `models.py`: 包含用于通信的数据模型（例如 `UserTask`、`AgentResponse`）。
*   `topics.py`: 定义用于在智能体之间路由消息的主题类型。
*   `tools.py`: 定义智能体可以执行的工具（例如 `execute_order_tool`）。
*   `tools_delegate.py`: 定义专门用于将对话委托/转移给其他智能体的工具。
*   `README.md`: (本文档) 项目介绍和使用说明。
*   `static/`: 包含 Web UI 的静态文件（例如 `index.html`）。
*   `model_config_template.yaml`: 模型配置文件的模板。

## **安装**

首先，请确保您已安装 Python（建议 3.8 或更高版本）。然后，安装必要的库：

```bash
pip install "fastapi" "uvicorn[standard]" "autogen-core" "autogen-ext[openai]" "PyYAML"
```

## **配置**

在与本 README 文件相同的目录中创建一个名为 `model_config.yaml` 的新文件，以配置您的语言模型设置（例如 Azure OpenAI 详细信息）。使用 `model_config_template.yaml` 作为起点。

**注意**: 对于生产环境，请使用环境变量或其他秘密管理工具安全地管理 API 密钥，而不是将其硬编码在配置文件中。

## **运行应用程序**

在包含 `app.py` 的目录中，运行以下命令以启动 FastAPI 应用程序：

```bash
uvicorn app:app --host 0.0.0.0 --port 8501 --reload
```

应用程序包含一个简单的 Web 界面。启动服务器后，在浏览器中导航到 `http://localhost:8501`。

聊天完成的 API 端点将位于 `http://localhost:8501/chat/completions`。

## **使用 API**

您可以通过向 `/chat/completions` 端点发送 POST 请求与智能体系统进行交互。请求正文必须为 JSON 格式，并包含 `message` 字段（用户输入）和 `conversation_id` 字段以跟踪聊天会话。

**请求正文格式**:

```json
{
  "message": "我需要退款。",
  "conversation_id": "user123_session456"
}
```

**示例 (使用 curl)**:

```bash
curl -N -X POST http://localhost:8501/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "message": "你好，我买了一辆火箭动力独轮车，它爆炸了。",
  "conversation_id": "wile_e_coyote_1"
}'
```

**示例 (使用 Python requests)**:

```python
import requests
import json
import uuid

url = "http://localhost:8501/chat/completions"
conversation_id = f"conv-id" # 为不同的会话生成唯一的对话 ID。

def send_message(message_text):
    data = {
        'message': message_text,
        'conversation_id': conversation_id
    }
    headers = {'Content-Type': 'application/json'}
    try:
        print(f"\n>>> 用户: {message_text}")
        print("<<< 助手: ", end="", flush=True)
        response = requests.post(url, json=data, headers=headers, stream=True)
        response.raise_for_status()
        full_response = ""
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                try:
                    # Decode the chunk
                    chunk_str = chunk.decode('utf-8')
                    # Handle potential multiple JSON objects in a single chunk
                    for line in chunk_str.strip().split('\n'):
                        if line:
                            data = json.loads(line)
                            # Check the new structure
                            if 'content' in data and isinstance(data['content'], dict) and 'message' in data['content']:
                                message_content = data['content']['message']
                                message_type = data['content'].get('type', 'string') # Default to string if type is missing

                                # Print based on type (optional, could just print message_content)
                                if message_type == 'function':
                                    print(f"[{message_type.upper()}] {message_content}", end='\n', flush=True) # Print function calls on new lines for clarity
                                    print("<<< 助手: ", end="", flush=True) # Reprint prefix for next string part
                                else:
                                    print(message_content, end='', flush=True)

                                full_response += message_content # Append only the message part
                            else:
                                print(f"\nUnexpected chunk format: {line}")

                except json.JSONDecodeError:
                    print(f"\nError decoding chunk/line: '{line if 'line' in locals() else chunk_str}'")

        print("\n--- 响应结束 ---")
        return full_response

    except requests.exceptions.RequestException as e:
        print(f"\n错误: {e}")
    except Exception as e:
        print(f"\n发生意外错误: {e}")

# 开始对话
send_message("我需要退款")
# 继续对话 (示例)
# send_message("我想要我的朋友 Amith 买的火箭。")
# send_message("它们是 SpaceX 3000 型号。")
# send_message("听起来很棒，我买了！")
# send_message("是的，我同意价格和注意事项。")


```
