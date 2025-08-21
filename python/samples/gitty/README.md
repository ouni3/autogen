# **gitty (警告：WIP - 正在进行中)**

这是一个由 AutoGen 驱动的命令行界面（CLI）工具，旨在为 GitHub 上的 Issues 和 Pull Requests 生成草稿回复，以减少开源项目的维护开销。

## **功能说明**

`gitty` 的核心功能是自动化生成针对 GitHub Issues 和 Pull Requests 的回复草稿。这有助于项目维护者更高效地处理社区贡献和问题报告。

### **主要功能**

*   **自动化回复生成**: 利用 AutoGen 的能力，根据 Issue 或 Pull Request 的内容自动生成初步的回复草稿。
*   **减少维护开销**: 旨在通过自动化部分回复流程，减轻开源项目维护者的工作负担。
*   **命令行接口**: 提供一个简单的 CLI 接口，方便用户直接在终端中操作。

### **使用示例**

*   **生成 Issue 回复**:
    ```bash
    gitty --repo microsoft/autogen issue 5212
    ```
    此命令将为 `microsoft/autogen` 仓库的第 5212 号 Issue 生成一个草稿回复。

## **安装与配置**

### **1. 安装依赖**

首先，请确保您已安装 `uv`（一个快速的 Python 包安装器和解析器）。然后，在项目根目录中运行以下命令来安装所有依赖项：

```bash
uv sync --all-extras
```

### **2. 激活虚拟环境**

安装完成后，激活您的 Python 虚拟环境：

```bash
source .venv/bin/activate
```

### **3. 设置 OpenAI API 密钥**

`gitty` 需要访问 OpenAI API 来生成回复。请设置 `OPENAI_API_KEY` 环境变量：

```bash
export OPENAI_API_KEY=sk-.... # 替换为您的实际 OpenAI API 密钥
```

**注意**: 这是一个正在进行中的项目（WIP），功能可能仍在开发和完善中。
