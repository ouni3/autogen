# 使用 FastAPI 构建 AgentChat 应用

本示例项目展示了如何结合使用 Microsoft 的 [AutoGen AgentChat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html) 框架与 [FastAPI](https://fastapi.tiangolo.com/) 来构建功能丰富的实时聊天应用程序。项目提供了两种核心模式：单智能体聊天和多智能体团队协作聊天。

## **项目概述**

本项目包含两个独立的 FastAPI 应用，它们分别演示了 AgentChat 在不同场景下的应用：

1.  **`app_agent.py` (单智能体聊天)**:
    *   此应用启动一个 FastAPI 服务器，允许用户通过一个简洁的浏览器界面与单个 `AssistantAgent` 进行实时交互。用户可以输入消息，智能体将回复，模拟一个一对一的对话体验。
    *   服务器默认运行在 `http://localhost:8001`。

2.  **`app_team.py` (智能体团队聊天)**:
    *   此应用启动一个 FastAPI 服务器，支持用户与一个由多个智能体组成的团队进行协作对话。用户可以参与到由多个智能体组成的对话流程中，体验团队协作的动态。
    *   团队采用 `RoundRobinGroupChat`（轮询群聊）策略，确保团队中的每个智能体（包括代表用户的 `UserProxyAgent`）都能按顺序发言。
    *   当轮到用户输入时，浏览器界面上的文本输入框将激活，允许用户输入消息并加入到团队的讨论中。
    *   服务器默认运行在 `http://localhost:8002`。

## **主要功能**

本项目提供了以下核心用户功能：

*   **实时一对一聊天**: 与单个 AI 智能体进行流畅的实时对话。
*   **智能体团队协作**: 参与由多个 AI 智能体组成的团队对话，体验轮流发言的协作模式。
*   **对话历史记录**: 自动保存和加载对话历史，允许用户在服务器重启后继续之前的对话。
*   **可配置的 AI 模型**: 用户可以根据自己的需求和偏好，通过 `model_config.yaml` 文件轻松配置使用的语言模型（LLM），包括本地模型或云服务模型。
*   **Web 界面交互**: 通过简单的 Web 浏览器界面与 AI 智能体进行交互，无需复杂的命令行操作。

### **核心技术特性**

*   **智能体 (Agents)**:
    *   `AssistantAgent`: 作为助手角色，负责执行任务和提供信息。
    *   `UserProxyAgent`: 代表用户与智能体进行交互，通过自定义的 WebSocket 函数接收来自浏览器界面的用户输入。
*   **团队协作机制**:
    *   `RoundRobinGroupChat`: 实现智能体之间的轮流对话机制，模拟团队协作流程。
*   **状态持久化**:
    *   通过 `save_state` 和 `load_state` 方法，智能体和团队的状态（包括对话历史、配置等）会在每次交互后持久化到 JSON 文件中（例如 `agent_state.json` 和 `team_state.json`），确保对话的连续性。
*   **模型配置**:
    *   支持灵活的模型配置，允许用户根据需求选择不同的语言模型（LLM）。
    *   通过 `model_config.yaml` 文件进行配置，并提供 `model_config_template.yaml` 作为配置模板参考。

## **安装与配置指南**

### **1. 安装项目依赖**

在开始之前，请确保您已安装 Python 3.7 或更高版本。然后，使用以下命令安装所有必需的软件包，包括对 OpenAI 的支持：

```bash
pip install -U "autogen-agentchat" "autogen-ext[openai]" "fastapi" "uvicorn[standard]" "PyYAML"
```

如果您希望使用 OpenAI 以外的语言模型，请参考 [AutoGen 模型文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html) 以获取详细的配置说明。

### **2. 配置语言模型 (LLM)**

为了使 AgentChat 能够正常工作，您需要配置语言模型。请在项目根目录下创建一个名为 `model_config.yaml` 的文件。您可以参考提供的 `model_config_template.yaml` 文件来了解配置结构和示例。

**`model_config.yaml` 示例结构 (请根据您的实际模型和 API Key 进行修改):**

```yaml
# model_config_template.yaml 示例
# 请根据您的实际情况修改此文件，例如 OpenAI API Key 和模型名称

# OpenAI 配置示例
# config_list:
#   - {model: "gpt-4", api_key: "YOUR_OPENAI_API_KEY"}
#   - {model: "gpt-3.5-turbo", api_key: "YOUR_OPENAI_API_KEY"}

# 其他模型配置示例 (如 Azure OpenAI, Ollama 等)
# 请参考 AutoGen 文档以获取更多模型配置选项

# 示例：使用本地 Ollama 模型
# config_list:
#   - {model: "llama3", base_url: "http://localhost:11434/v1", api_key: "ollama"}
```

**重要提示**:
*   请确保您的 `model_config.yaml` 文件中包含了有效的语言模型配置，特别是 API 密钥（如果需要）。
*   **强烈建议**将敏感信息（如 API 密钥）存储在 `.env` 文件中，并在 `.gitignore` 文件中排除 `.env`，以防止意外泄露。虽然本项目当前 README 未明确提及 `.env` 文件，但这是业界标准的安全实践。

## **运行应用**

### **启动单智能体聊天应用**

要启动单智能体聊天的 FastAPI 服务器，请在项目根目录下执行以下命令：

```bash
python app_agent.py
```

服务器启动后，您可以通过浏览器访问 `http://localhost:8001` 来开始与智能体聊天。

### **启动智能体团队聊天应用**

要启动支持团队协作的 FastAPI 服务器，请在项目根目录下执行以下命令：

```bash
python app_team.py
```

服务器启动后，您可以通过浏览器访问 `http://localhost:8002` 来与智能体团队进行交互。

## **项目结构**

以下是项目的主要文件和目录及其作用：

*   `app_agent.py`: 单智能体聊天应用的 FastAPI 服务器实现。
*   `app_team.py`: 多智能体团队聊天应用的 FastAPI 服务器实现。
*   `README.md`: 本项目说明文档。
*   `requirements.txt`: 项目所需的 Python 依赖列表。
*   `model_config_template.yaml`: 语言模型配置模板文件。
*   `agent_state.json`: 单智能体聊天应用的状态持久化文件。
*   `team_state.json`: 智能体团队聊天应用的状态持久化文件。
*   `agent_history.json`: 单智能体聊天应用的对话历史记录文件（用于前端显示）。
*   `team_history.json`: 智能体团队聊天应用的对话历史记录文件（用于前端显示）。
*   `Dockerfile`: (可选) 用于将应用容器化的 Docker 配置文件。

## **故障排除**

*   **端口冲突**: 如果 `8001` 或 `8002` 端口已被占用，您可能需要更改应用的监听端口。这通常可以通过修改 `app_agent.py` 和 `app_team.py` 中 `uvicorn.run` 函数的 `port` 参数来实现。
*   **模型配置错误**: 确保 `model_config.yaml` 文件格式正确，并且包含有效的语言模型 API 密钥和模型名称。检查 AutoGen 的文档以获取正确的配置格式。
*   **依赖问题**: 如果遇到依赖安装问题，请尝试使用 `pip install --upgrade --force-reinstall -r requirements.txt` 命令重新安装所有依赖。
*   **状态文件损坏**: 如果应用行为异常，可以尝试删除 `agent_state.json`, `team_state.json`, `agent_history.json`, `team_history.json` 等状态文件，然后重启应用。这将导致对话从头开始。

## **贡献指南**

欢迎为本项目贡献代码和改进建议！请遵循以下步骤：

1.  Fork 本项目。
2.  创建新的特性分支 (`git checkout -b feature/YourFeature`)。
3.  提交您的更改 (`git commit -am 'Add YourFeature'`)。
4.  将更改推送到分支 (`git push origin feature/YourFeature`)。
5.  创建 Pull Request。

## **许可证**

本项目采用 [MIT 许可证](LICENSE)。


关于智能体团队聊天（`app_team.py`）的详细内容和操作如下：

**核心功能与架构：**

*   **服务器设置**: 该应用是一个 FastAPI 服务器，默认运行在 `http://localhost:8002`。它通过 WebSocket (`/ws/chat`) 接收用户消息并返回智能体回复。
*   **智能体组成**: 团队由以下智能体组成：
    *   一个名为 "assistant" 的通用助手 (`AssistantAgent`)。
    *   一个名为 "yoda" 的模仿尤达语气的助手 (`AssistantAgent`)。
    *   一个名为 "user" 的用户代理 (`UserProxyAgent`)，它负责接收来自浏览器界面的用户输入。
*   **团队协作机制**: 团队使用 `RoundRobinGroupChat`（轮询群聊）策略，这意味着团队中的每个成员（包括用户代理）会按顺序发言，模拟一个协作流程。
*   **模型配置**: 应用从 `model_config.yaml` 文件加载语言模型（LLM）的配置，允许用户自定义使用的模型。
*   **状态与历史持久化**:
    *   智能体团队的状态（包括对话上下文）会在每次交互后保存到 `team_state.json` 文件中，以便在服务器重启后恢复。
    *   对话历史记录会保存到 `team_history.json` 文件中，用于前端显示。
*   **Web 界面**: 应用提供了一个简单的 Web 界面 (`app_team.html`)，用户可以通过浏览器访问 `http://localhost:8002` 来与智能体团队进行交互。

**操作流程：**

1.  用户通过浏览器访问 `http://localhost:8002`。
2.  浏览器建立 WebSocket 连接到 `/ws/chat`。
3.  用户在界面输入消息，并通过 WebSocket 发送给服务器。
4.  服务器接收到用户消息后，调用 `get_team` 函数加载模型配置和团队状态。
5.  `team.run_stream(task=request)` 方法被调用，将用户消息传递给团队中的智能体进行处理。
6.  智能体（"assistant" 和 "yoda"）根据轮询顺序生成回复。
7.  生成的回复通过 WebSocket 流式传输回用户的浏览器界面。
8.  每次交互后，团队的状态和对话历史都会被保存。