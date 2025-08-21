# **AgentChat 国际象棋游戏**

这是一个简单的国际象棋游戏，您可以与 AI 智能体对战。

## **功能说明**

本示例通过 `main.py` 脚本启动一个国际象棋游戏。游戏支持两种模式：

1.  **AI 对战随机智能体 (默认模式)**: 在此模式下，一个 AI 智能体将与一个每步都随机移动的智能体进行对战。
2.  **人机对战模式**: 通过添加 `--human` 标志，您可以亲自与 AI 智能体进行对战。

AI 智能体利用大语言模型（LLM）来理解棋局并做出决策。

## **安装与配置**

### **1. 安装依赖**

首先，请确保您已安装所有必需的 Python 包：

```bash
pip install "chess" "autogen-ext[openai]" autogen-agentchat pyyaml
```

*   `chess`: 用于处理国际象棋逻辑。
*   `autogen-ext[openai]`: 用于连接 OpenAI 模型或兼容 OpenAI API 的终结点。如果您使用 Azure OpenAI，请安装 `"autogen-ext[openai,azure]"`。
*   `autogen-agentchat` 和 `pyyaml`: AutoGen 的核心组件和配置所需。

### **2. 配置模型**

在脚本所在的目录中，创建一个名为 `model_config.yaml` 的文件，用于配置您希望使用的语言模型。

以下是一些配置示例：

**使用 OpenAI 的 gpt-4o 模型:**

```yaml
provider: autogen_ext.models.openai.OpenAIChatCompletionClient
config:
  model: gpt-4o
  api_key: "sk-..." # 替换为您的 API 密钥，或设置 OPENAI_API_KEY 环境变量
```

**使用本地通过 Ollama 托管的 DeepSeek-R1:8b 模型:**

```yaml
provider: autogen_ext.models.openai.OpenAIChatCompletionClient
config:
  model: deepseek-r1:8b
  base_url: http://localhost:11434/v1
  api_key: ollama
  model_info:
    function_calling: false
    json_output: false
    vision: false
    family: r1
```

有关如何配置模型和使用其他提供商的更多信息，请参阅[模型文档](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html)。

## **运行游戏**

### **AI 对战随机智能体**

运行以下命令以启动默认模式的游戏：

```bash
python main.py
```

### **人机对战**

要启用人机对战模式，请使用 `--human` 标志：

```bash
python main.py --human
```
