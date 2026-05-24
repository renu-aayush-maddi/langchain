from langchain.chat_models import ChatOpenAI
from pydantic.dataclasses import dataclass

@dataclass
class ContactInfo:
    name: str
    email: str
    phone: str

llm = ChatOpenAI(model='gpt-4.1-mini', temperature=0)
print('has_with_structured_output', hasattr(llm, 'with_structured_output'))
wrapped = llm.with_structured_output(ContactInfo)
print('wrapped_type', type(wrapped))
print('callable', callable(wrapped))
