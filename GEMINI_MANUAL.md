# AutoGen Gemini 模型测试操作手册

本文档将指导您如何配置和运行本项目，以测试通过 AutoGen 框架与 Gemini 模型的集成。

## 1. 环境准备

在开始之前，请确保您已经安装了 Python 3.10 或更高版本，并已根据项目 `README.md` 的指引安装了必要的依赖库。主要包括：

```bash
pip install -U "autogen-agentchat" "autogen-ext[openai]" python-dotenv
```

## 2. 环境变量配置

项目需要通过 `.env` 文件来加载 Gemini 模型的 API 配置。

1.  在项目根目录下找到或创建一个名为 `.env` 的文件。
2.  打开 `.env` 文件，并根据您的实际情况修改以下内容：

    ```dotenv
    # .env file for AutoGen Gemini configuration

    # 请将 YOUR_BASE_URL 替换为您的中转接口地址
    BASE_URL="http://192.168.0.100:8000/v1"

    # 您的 API 密钥
    # 如果您的中转服务不需要, 可以设置为任意值, 例如: "dummy-key"
    API_KEY="sk-123456"
    ```

    -   `BASE_URL`: 这是您访问 Gemini 模型的接口地址。请确保该地址可以被您的运行环境访问。
    -   `API_KEY`: 这是您的 API 密钥。

## 3. 运行测试脚本

您可以通过以下两种方式运行测试脚本：

### 方式一：直接运行 Python 脚本

打开您的终端，并执行以下命令：

```bash
python run_gemini_with_env.py
```

### 方式二：使用我们为您准备的测试脚本

为了方便测试，我们提供了 `test_gemini.bat` (适用于 Windows) 和 `test_gemini.sh` (适用于 Linux/macOS) 脚本。

**对于 Windows 用户：**

直接在文件浏览器中双击 `test_gemini.bat` 文件，或者在终端中执行：

```bash
.\test_gemini.bat
```

**对于 Linux/macOS 用户：**

首先，需要给脚本添加可执行权限：

```bash
chmod +x test_gemini.sh
```

然后，运行脚本：

```bash
./test_gemini.sh
```

## 4. 预期输出

当脚本成功执行后，您将在终端看到类似以下的输出：

```
向模型提问: 你好，请用中文介绍一下你自己以及你的能力。

模型回答:
[模型的自我介绍内容]

客户端连接已关闭。
```

如果看到模型的回答，即表示您已成功配置并运行了本项目。

如果出现错误，请根据终端中的错误提示检查您的 `.env` 文件配置以及网络连接。
