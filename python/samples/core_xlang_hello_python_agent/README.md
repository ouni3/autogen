# **Python 和 .NET 智能体互操作性示例**

本示例演示了如何创建一个 Python 智能体，使其能够与一个 .NET 智能体进行交互，从而展示 AutoGen 框架的跨语言通信能力。

## **功能说明**

本示例的核心功能是实现 Python 和 .NET 智能体之间的无缝通信。它通过以下组件和流程来完成：

*   **.NET Aspire 应用主机 (Hello.AppHost)**: 这是一个 .NET Aspire 应用程序主机，负责启动和管理多个项目：
    *   **后端 (.NET 智能体运行时)**: 提供 .NET 智能体的运行环境和通信基础设施。
    *   **HelloAgent (.NET 智能体)**: 一个用 .NET 编写的智能体，它将接收来自 Python 智能体的消息并进行处理。
    *   **`hello_python_agent.py` (Python 智能体)**: 本示例中的 Python 智能体，它将向 .NET 运行时发送消息。
*   **跨语言消息传递**: Python 智能体通过向 .NET 运行时发送消息来与 .NET 智能体进行交互。然后，.NET 运行时会将这些消息中继到相应的 .NET 智能体。这展示了 AutoGen 如何在不同编程语言编写的智能体之间建立通信桥梁。
*   **Aspire Dashboard**: 应用主机启动后，会在 `https://localhost:15887` 启动 Aspire Dashboard，您可以在其中监控各个服务的状态。

这个示例强调了 AutoGen 在构建多语言、分布式智能体系统方面的灵活性和强大功能。

## **运行示例**

要运行此示例，请首先克隆 AutoGen 仓库。然后按照以下步骤操作：

1.  导航到 `autogen/dotnet/samples/Hello/Hello.AppHost` 目录。
2.  运行 `dotnet run` 命令以启动 .NET Aspire 应用主机。这将同时启动后端（.NET 智能体运行时）、HelloAgent（.NET 智能体）以及本示例中的 Python 智能体 `hello_python_agent.py`。
3.  应用主机将在 `https://localhost:15887` 启动 Aspire Dashboard，您可以在浏览器中访问它以查看应用程序的状态。

Python 智能体将自动开始与 .NET 智能体进行交互，通过向 .NET 运行时发送消息，然后由运行时将消息中继到 .NET 智能体。
