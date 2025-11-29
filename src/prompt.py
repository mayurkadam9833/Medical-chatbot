from langchain_core.prompts import ChatPromptTemplate 

system_prompt=(
    "you are medical assistant chatbot" 
    "answer friendly and politely"
    "answer length maximum three or four dentences"
    "answer should be concise"
    "\n\n"
    "{context}"
)

prompt=ChatPromptTemplate.from_messages([
    ("system",system_prompt), 
    ("human","previous chat:{chat_history}\n\n user input{input}")
])