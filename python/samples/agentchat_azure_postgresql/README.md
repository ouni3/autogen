# **使用 AutoGen 和 Azure PostgreSQL 构建多智能体 PostgreSQL 数据管理系统**

本项目演示了如何使用 AutoGen、Azure OpenAI GPT-4 和 Azure PostgreSQL 构建一个多智能体 AI 系统，用于管理存储在 Azure PostgreSQL 数据库中的货运数据。

这个应用的核心目标是展示如何让多个 AI 智能体协同工作，不仅能回答关于数据的问题，还能根据用户需求修改数据，甚至创建和使用新的数据库存储过程。它将传统的“与数据聊天”扩展到了“与数据聊天、对数据执行操作和编码”。

## **核心技术**

*   **AutoGen**: 用于协调 AI 智能体在协作工作流程中的工作。
*   **Azure OpenAI GPT-4**: 用于智能语言理解和生成 PostgreSQL 的 SQL 查询。
*   **Azure Database for PostgreSQL**: 用于数据存储和查询。

## **功能特性**

*   **🤖 多智能体系统**: 多个智能体协作处理特定任务：
    *   **SchemaAgent**: 管理数据库模式的检索和共享，并被授权创建存储过程。
    *   **ShipmentAgent**: 处理与货运相关的查询和更新。
    *   **CRMAgent**: 管理客户和产品相关的数据。
*   **🧠 Azure OpenAI GPT-4**: 生成 SQL 查询和自然语言响应。
*   **🛢️ Azure PostgreSQL**: 存储货运、客户和产品数据。

## **系统架构**

系统采用模块化设计，以便于通过即插即用的方式进行测试和进一步扩展：

*   `pg_utils.py`: 提供一个类和工具，使智能体能够连接到数据库并执行各种任务。
*   `agent_tools.py`: 包含创建所需专家智能体的函数。
*   `multi_agent_chats.py`: 提供一个类来初始化各种类型的群聊（即团队）。

## **如何开始**

要运行此示例，您需要访问以下 GitHub 仓库，并按照其中的说明进行操作。该仓库包含了完整的源代码和设置指南。

[MultiAgent_Azure_PostgreSQL_AutoGen 示例仓库](https://github.com/Azure-Samples/MultiAgent_Azure_PostgreSQL_AutoGen0.4/tree/main)
