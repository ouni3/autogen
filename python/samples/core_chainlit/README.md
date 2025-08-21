# **Core Chainlit 集成示例**

本示例演示了如何使用 [Chainlit](https://github.com/Chainlit/chainlit) 构建一个简单的聊天界面，该界面可以与 [AutoGen Core](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/index.html) 智能体或智能体团队进行交互，并支持流式消息传输。

## **功能说明**

`core_chainlit` 示例旨在展示 Chainlit 与单线程智能体运行时集成的简单用例。它包括以下组件和功能：

*   **单智能体**: 一个在 Chainlit 环境中运行的单个智能体。
*   **群聊**: 一个包含两个智能体的群聊设置：
    *   **助手智能体 (Assistant Agent)**: 负责响应用户输入。
    *   **评论智能体 (Critic Agent)**: 对助手智能体的响应进行反思和评论。
*   **闭包智能体 (Closure Agent)**: 利用闭包智能体将输出消息聚合到输出队列中。
*   **令牌流式传输**: 演示如何将令牌流式传输到用户界面，提供实时响应体验。
*   **会话管理**: 在 Chainlit 用户会话中管理运行时和输出队列。

## **安装与配置**

### **1. 环境要求**

要运行此示例，您需要：

*   Python 3.8 或更高版本。
*   安装 `requirements.txt` 中列出的必要 Python 包。

### **2. 安装依赖**

运行以下命令安装所需的软件包：

```shell
pip install -U chainlit autogen-core autogen-ext[openai] pyyaml
```

要使用其他模型提供商，您需要为 `autogen-ext` 包安装不同的附加功能。有关更多信息，请参阅[模型文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html)。

### **3. 模型配置**

创建一个名为 `model_config.yaml` 的配置文件来配置您要使用的模型。请使用 `model_config_template.yaml` 作为模板。

## **运行示例**

### **1. 运行单智能体示例**

此示例演示如何从聊天界面与单个 `AssistantAgent` 进行交互。请先 `cd` 到示例目录。

```shell
chainlit run app_agent.py
```

### **2. 运行团队示例**

此示例演示如何从聊天界面与一个智能体团队进行交互。

```shell
chainlit run app_team.py -h
```

团队中有两个智能体：一个通常提供帮助，另一个则扮演评论家角色并提供反馈。
