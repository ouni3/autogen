# **Core gRPC 工作运行时示例**

本示例演示了 AutoGen Core 中基于 gRPC 的工作运行时（Worker Runtime）的发布/订阅（Pub/Sub）和远程过程调用（RPC）机制。它展示了如何设置一个 gRPC 主机，以及如何通过分布式工作运行时连接和管理智能体。

## **功能说明**

本示例主要通过以下几个脚本来展示 gRPC 工作运行时的不同方面：

*   **`run_host.py`**: 启动 gRPC 服务器，作为所有分布式工作运行时的中央主机。它负责监听来自智能体的连接请求，并协调消息的发布和订阅。
*   **`agents.py`**: 定义了示例中使用的智能体：
    *   **`CascadingAgent`**: 演示了消息的级联发布。它接收一个 `CascadingMessage`，发布一个 `ReceiveMessageEvent`，并在达到预设的最大轮次之前，继续发布下一个 `CascadingMessage`。这模拟了消息在智能体之间传递的链式反应。
    *   **`ObserverAgent`**: 作为一个观察者，它订阅 `ReceiveMessageEvent` 并打印出消息的详细信息，用于监控消息流。
*   **`run_worker_pub_sub.py`**: 演示了如何通过 gRPC 工作运行时实现发布/订阅模式。智能体可以向特定主题发布消息，而其他智能体可以订阅这些主题以接收消息。
*   **`run_worker_rpc.py`**: 演示了如何通过 gRPC 工作运行时实现远程过程调用（RPC）。智能体可以调用远程智能体上定义的方法，实现直接的智能体间通信。
*   **`run_cascading_worker.py`**: 启动一个或多个 `CascadingAgent` 实例，连接到 gRPC 主机，并开始级联消息的发布过程。
*   **`run_cascading_publisher.py`**: 启动一个 `CascadingAgent` 实例，作为级联消息的初始发布者。

这个示例强调了 AutoGen Core 在构建可扩展、分布式多智能体系统方面的能力，通过 gRPC 实现了高效的跨进程通信。

## **安装与配置**

### **1. 安装依赖**

首先，请确保您已安装所有必需的 Python 包：

```bash
pip install autogen-core grpcio grpcio-tools pyyaml
```

### **2. 模型配置**

本示例可能不需要复杂的模型配置，但如果智能体需要调用 LLM，您可能需要在本地创建一个 `model_config.yml` 文件来配置语言模型。

## **运行示例**

要运行此示例，您需要按照以下步骤在不同的终端中启动各个组件：

1.  **启动 gRPC 主机**:
    ```bash
    python run_host.py
    ```
2.  **启动发布/订阅工作运行时 (可选)**:
    ```bash
    python run_worker_pub_sub.py
    ```
3.  **启动 RPC 工作运行时 (可选)**:
    ```bash
    python run_worker_rpc.py
    ```
4.  **启动级联发布者**:
    ```bash
    python run_cascading_publisher.py
    ```
5.  **启动级联工作运行时 (可选，用于观察级联消息)**:
    ```bash
    python run_cascading_worker.py
    ```

请注意，您可能需要根据您的具体需求和测试场景来选择运行哪些脚本。
