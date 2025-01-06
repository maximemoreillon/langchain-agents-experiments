from langchain_openai import ChatOpenAI
from langchain_community.tools.shell.tool import ShellTool
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent


# Create the agent
model = ChatOpenAI(model="gpt-4o-mini")
search = ShellTool(ask_human_input=True)
tools = [search]
agent_executor = create_react_agent(model, tools)

# Use the agent
response = agent_executor.invoke(
    {"messages": [HumanMessage(content="What is my OS?")]}
)
print(response["messages"])
