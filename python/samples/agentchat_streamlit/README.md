# **使用 Streamlit 构建 AgentChat 应用**

这是一个使用 [Streamlit](https://streamlit.io/) 构建的 AI 聊天助手示例应用。

## **功能说明**

本示例通过 `main.py` 脚本启动一个 Streamlit Web 应用，提供一个用户友好的聊天界面。用户可以在此界面中与一个由 AutoGen `AssistantAgent` 驱动的 AI 助手进行实时对话。

应用的主要功能包括：

*   **交互式聊天界面**: 利用 Streamlit 构建，界面简洁直观。
*   **AI 智能体集成**: 后端集成了一个 `AssistantAgent`，负责处理用户的输入并生成响应。
*   **流式响应**: 智能体的回复会以流式的方式显示在界面上，提升了用户体验。
*   **对话历史**: 聊天记录会保存在会话状态中，并在界面上展示。

## **安装与配置**

### **1. 安装依赖**

首先，请确保您已安装所有必需的 Python 包：

```bash
pip install streamlit "autogen-ext[openai,azure]"
```

*   `streamlit`: 用于构建和运行 Web 应用。
*   `autogen-ext[openai,azure]`: 用于连接 Azure OpenAI 模型或兼容 OpenAI API 的终结点。如果您仅使用 OpenAI，可以安装 `"autogen-ext[openai]"`。

### **2. 配置模型**

在脚本所在的目录中，创建一个名为 `model_config.yml` 的文件，用于配置您希望使用的语言模型。

**示例：使用 Azure OpenAI 的 gpt-4o-mini 模型**

```yml
provider: autogen_ext.models.openai.AzureOpenAIChatCompletionClient
config:
  azure_deployment: "gpt-4o-mini"
  model: gpt-4o-mini
  api_version: "YOUR_API_VERSION"
  azure_endpoint: "YOUR_ENDPOINT"
  api_key: "YOUR_API_KEY"
```

请将 `REPLACE_WITH_...` 占位符替换为您的实际凭据。

有关如何配置模型和使用其他提供商的更多信息，请参阅[模型文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html)。

## **运行应用**

运行以下命令以启动 Web 应用程序：

```bash
streamlit run main.py
```

应用启动后，Streamlit 会在您的默认浏览器中打开一个新的标签页，显示聊天界面。
