# **使用 AutoGen 和 Chainlit 构建多智能体应用**

本示例将演示如何使用 [Chainlit](https://github.com/Chainlit/chainlit) 构建一个简单的聊天界面，该界面可以与 [AgentChat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html) 的单个智能体或智能体团队进行交互，并支持流式消息传输。

## **功能说明**

本示例包含三个独立的应用程序，分别展示了与不同智能体配置的交互方式：

1.  **`app_agent.py`**: 与单个 `AssistantAgent` 进行交互。该智能体可以使用提供的工具来回答问题，例如查询西雅图的天气。
2.  **`app_team.py`**: 与一个由两个智能体组成的团队进行交互。这是一个轮询式（Round-Robin）的群聊，一个智能体负责提供有用的信息，另一个则扮演批评家的角色提供反馈。对话将以轮询方式进行，直到批评家智能体发出“APPROVE”指令。
3.  **`app_team_user_proxy.py`**: 与一个包含 `UserProxyAgent` 的智能体团队进行交互。`UserProxyAgent` 会请求用户批准或拒绝团队的响应。例如，当要求团队编写反转字符串的代码时，用户需要手动批准代码，然后 `UserProxyAgent` 才会向团队发送“APPROVE”消息以结束对话。

## **安装**

要运行此示例，您需要安装以下软件包：

```shell
pip install -U chainlit autogen-agentchat "autogen-ext[openai]" pyyaml
```

要使用其他模型提供商，您需要为 `autogen-ext` 包安装不同的附加功能。有关更多信息，请参阅[模型文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html)。

## **模型配置**

创建一个名为 `model_config.yaml` 的配置文件来配置您要使用的模型。请使用 `model_config_template.yaml` 作为模板。

## **运行示例**

### **1. 单智能体示例**

此示例演示如何从聊天界面与单个 `AssistantAgent` 进行交互。

```shell
chainlit run app_agent.py -h
```

您可以使用其中一个起始问题，例如，提问“西雅图的天气怎么样？”。智能体将首先使用提供的工具，然后对工具执行的结果进行反思并作出回应。

### **2. 智能体团队示例**

此示例演示如何从聊天界面与一个智能体团队进行交互。

```shell
chainlit run app_team.py -h
```

您可以使用其中一个起始问题，例如，提问“写一首关于冬天的诗。”。该团队是一个 `RoundRobinGroupChat`，因此每个智能体都会轮流响应。

### **3. 带 UserProxyAgent 的智能体团队示例**

此示例演示如何与一个包含 `UserProxyAgent` 的智能体团队进行交互，以实现批准或拒绝功能。

```shell
chainlit run app_team_user_proxy.py -h
```

您可以使用其中一个起始问题，例如，提问“编写代码来反转一个字符串。”。默认情况下，`UserProxyAgent` 会请求用户输入操作来批准或拒绝团队的响应。

## **后续步骤**

您可以通过以下几种方式扩展此示例：

*   尝试其他类型的[智能体](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html)。
*   尝试除 `RoundRobinGroupChat` 之外的其他[团队类型](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html)。
*   探索发送多模态消息的自定义智能体。
