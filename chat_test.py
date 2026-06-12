from utils.chatbot import answer_question

context = """
The Right to Information Act allows citizens to request
information from public authorities.
"""

question = "Who can request information?"

print(answer_question(context, question))