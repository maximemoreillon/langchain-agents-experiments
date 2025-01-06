from langchain_openai import ChatOpenAI
from langchain_community.tools.shell.tool import ShellTool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent


# Create the agent
memory = MemorySaver()
model = ChatOpenAI(model="gpt-4o-mini")
search = ShellTool(ask_human_input=True)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
config = {"configurable": {"thread_id": "abc123"}}
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="Please find out what OS I am running")]}, config
):
    print(chunk)
    print("----")

