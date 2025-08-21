# **使用 FastAPI 构建 AgentChat 应用**

本示例演示了如何使用 [AgentChat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html) 和 [FastAPI](https://fastapi.tiangolo.com/) 创建一个简单的聊天应用程序。

## **功能说明**

本示例包含两个独立的 FastAPI 应用，分别展示了不同的 AgentChat 功能：

1.  **`app_agent.py` (单智能体聊天)**:
    *   启动一个 FastAPI 服务器，允许用户通过浏览器与单个 `AssistantAgent` 进行实时聊天。
    *   服务器运行在 `http://localhost:8001`。

2.  **`app_team.py` (智能体团队聊天)**:
    *   启动一个 FastAPI 服务器，允许用户与一个由多个智能体组成的团队进行交互。
    *   该团队采用 `RoundRobinGroupChat`（轮询群聊）模式，团队中的每个智能体（包括代表用户的 `UserProxyAgent`）将轮流发言。
    *   当轮到用户发言时，浏览器中的输入框将变为可用状态。
    *   服务器运行在 `http://localhost:8002`。

### **核心特性**

*   **智能体**:
    *   `AssistantAgent`: 扮演助手的角色。
    *   `UserProxyAgent`: 代表用户，通过自定义的 WebSocket 函数从浏览器接收输入。
*   **团队**: `RoundRobinGroupChat`，实现轮流对话。
*   **状态持久化**:
    *   智能体和团队的状态（如对话历史）在每次交互后都会通过 `save_state` 方法保存到 JSON 文件中（`agent_state.json` 和 `team_state.json`）。
    *   当服务器重启时，会通过 `load_state` 方法从这些文件中加载状态，从而实现跨会话的连续性。
    *   另外，`agent_history.json` 和 `team_history.json` 用于存储在浏览器中显示的对话历史。

## **安装与配置**

### **1. 安装依赖**

使用以下命令安装所有必需的软件包（包含 OpenAI 支持）：

```bash
pip install -U "autogen-agentchat" "autogen-ext[openai]" "fastapi" "uvicorn[standard]" "PyYAML"
```

要使用 OpenAI 以外的模型，请参阅[模型文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html)。

### **2. 配置模型**

在本 README 文件所在的目录中，创建一个名为 `model_config.yaml` 的文件来配置您的模型。可以参考 `model_config_template.yaml` 文件作为模板。

## **运行应用**

### **与单个智能体聊天**

要启动单智能体聊天的 FastAPI 服务器，请运行：

```bash
python app_agent.py
```

然后在浏览器中访问 `http://localhost:8001` 开始聊天。

### **与智能体团队聊天**

要启动团队聊天的 FastAPI 服务器，请运行：

```bash
python app_team.py
```

然后在浏览器中访问 `http://localhost:8002` 开始聊天。
