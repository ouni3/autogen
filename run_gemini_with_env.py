import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage

# 加载 .env 文件中的环境变量
load_dotenv()

async def main() -> None:
    """
    主函数，用于配置和运行基于 Gemini 模型的 AutoGen 智能体。
    """
    # 从环境变量中获取 API 配置
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")

    if not base_url or base_url == "YOUR_BASE_URL":
        print("错误: 请在 .env 文件中设置 BASE_URL。")
        return
    
    if not api_key or api_key == "YOUR_API_KEY":
        print("错误: 请在 .env 文件中设置 API_KEY。")
        return

    try:
        # 步骤 1: 使用从 .env 文件加载的配置来初始化客户端
        model_client = OpenAIChatCompletionClient(
            model="gemini-2.5-flash",
            base_url=base_url,
            api_key=api_key,
        )

        # 步骤 2: 创建 AssistantAgent 实例
        agent = AssistantAgent(
            name="gemini_assistant", 
            model_client=model_client
        )

        # 步骤 3: 定义任务并与智能体交互
        task = "你好，请用中文介绍一下你自己以及你的能力。"
        print(f"向模型提问: {task}")

        response = await agent.run(task=task)
        
        print("\n模型回答:")
        print(response)

    except Exception as e:
        print(f"在运行过程中发生错误: {e}")
    finally:
        # 步骤 4: 关闭客户端连接
        if 'model_client' in locals() and model_client:
            await model_client.close()
            print("\n客户端连接已关闭。")

if __name__ == "__main__":
    asyncio.run(main())
