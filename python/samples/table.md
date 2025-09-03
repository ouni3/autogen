
| 案例名称 (Sample Name) | 主要功能/目的 (Main Function/Purpose) | AutoGen 核心概念 (AutoGen Core Concept) | UI/交互方式 (UI/Interaction Method) | 集成/依赖 (Integrations/Dependencies) |
| :--- | :--- | :--- | :--- | :--- |
| `agentchat_azure_postgresql` | 使用多智能体系统管理 Azure PostgreSQL 数据库中的数据。 | `agentchat`, 多智能体系统 | 外部仓库中的演示应用 | Azure PostgreSQL |
| `agentchat_chainlit` | 为 AutoGen 智能体构建简单的 Web 聊天界面。包含单智能体、团队聊天和带用户代理的团队聊天等示例。 | `agentchat`, 群聊, `UserProxyAgent`, 流式响应, 工具使用 | Chainlit (Web UI) | Chainlit |
| `agentchat_chess_game` | 一个国际象棋游戏，用户（或随机智能体）可以与 AI 智能体对战。 | `agentchat`, 单智能体, 流式响应 | 命令行 (CLI) | `chess` 库 |
| `agentchat_dspy` | (文件为空) DSPy 集成示例，旨在展示如何将 DSPy 框架与 AutoGen 结合。 | `agentchat`, DSPy 集成 | - | DSPy |
| `agentchat_fastapi` | 使用 FastAPI 构建 Web API 服务。包含单智能体聊天和多智能体团队聊天，支持状态持久化和 WebSocket 交互。 | `agentchat`, 群聊, `UserProxyAgent`, 状态持久化, WebSocket 流式响应 | FastAPI (Web API + 前端) | FastAPI, uvicorn |
| `agentchat_graphrag` | 构建一个使用 GraphRAG 进行知识图谱检索增强生成 (RAG) 的 AI 助手。 | `agentchat`, RAG, 工具使用 (本地/全局搜索) | 命令行 (CLI) | GraphRAG |
| `agentchat_streamlit` | 使用 Streamlit 构建一个简单的 AI 聊天助手。 | `agentchat`, 单智能体 | Streamlit (Web UI) | Streamlit |
| `core_async_human_in_the_loop` | 演示一个异步“人在环路”系统，该系统可以暂停等待人类输入，保存状态，并在获得输入后恢复。 | `autogen-core`, 人在环路 (Human-in-the-Loop), 状态持久化 | 命令行 (CLI) | - |
| `core_chainlit` | `autogen-core` 版本的 Chainlit 集成，演示单智能体和团队聊天的流式响应。 | `autogen-core`, 群聊, 流式响应 | Chainlit (Web UI) | Chainlit |
| `core_chess_game` | 使用 `autogen-core` 实现的国际象棋游戏，智能体通过工具使用和反思来进行游戏。 | `autogen-core`, 工具智能体 (ToolAgent), 工具使用与反思 | 命令行 (CLI) | `chess` 库 |
| `core_distributed-group-chat` | 使用 gRPC 实现的分布式群聊系统，包含主机、多个智能体运行时（作者、编辑、经理）和一个 UI。 | `autogen-core`, 分布式智能体, gRPC, 群聊 | Chainlit (Web UI) + 多命令行 | gRPC, Chainlit |
| `core_grpc_worker_runtime` | `autogen-core` 分布式运行时的基础示例，演示主机/工作节点设置、发布/订阅和 RPC 模式。 | `autogen-core`, 分布式智能体, gRPC (Pub/Sub, RPC) | 命令行 (CLI) | gRPC |
| `core_semantic_router` | 演示如何根据用户意图（如 HR 或财务）将请求动态路由到最合适的智能体。 | `autogen-core`, 分布式智能体, 语义路由 | 命令行 (CLI) | gRPC |
| `core_streaming_handoffs_fastapi` | 一个 FastAPI 应用，演示流式响应和智能体之间的任务交接（例如，分诊 -> 销售 -> 维修），并支持持久化对话历史。 | `autogen-core`, 流式响应, 智能体任务交接 (Handoffs), 状态持久化 | FastAPI (Web API + 前端) | FastAPI |
| `core_streaming_response_fastapi` | 一个更简单的 FastAPI 应用，专注于实现智能体响应的流式传输。 | `autogen-core`, 流式响应 | FastAPI (Web API) | FastAPI |
| `core_xlang_hello_python_agent` | 演示 Python 智能体和 .NET 智能体之间通过 gRPC 进行跨语言互操作。 | `autogen-core`, 分布式智能体, 跨语言互操作 | 命令行 (CLI) | gRPC, .NET |
| `gitty` | 一个命令行工具，使用 AutoGen 为 GitHub 问题 (Issue) 生成回复草稿，以辅助开源项目维护。 | `agentchat`, 工具使用, RAG | 命令行 (CLI) | GitHub CLI, ChromaDB |
| `task_centric_memory` | 包含一系列评估脚本，用于测试智能体的记忆和学习能力（如可教性、自学、信息检索等）。 | `agentchat`, 可教智能体 (Teachable Agents), 记忆, RAG | 命令行 (CLI) | - |