import gradio as gr
from core.prompts import SYSTEM_PROMPT
from services.llm_client import LLMClient
from utils.logger import get_logger

logger = get_logger(__name__)

model = "gpt-4.1-mini"
llm = LLMClient(model=model)

def chat(message, history):
    """
    Docstring for chat
    
    This is a function that accepts the user input, track history and sends to the model to generate tokens
    """
    logger.info(f"User message received: {message}")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message}
    ]

    response = ""
    try:
        stream = llm.stream_chat(messages)
        for chunk in stream:
            response += chunk.choices[0].delta.content or ""
            yield response
    except Exception as e:
        logger.error(str(e))
        yield "Sorry, something went wrong."

gr.ChatInterface(
    fn=chat,
    title="Aphasia Assist (Prototype)",
    flagging_mode="never"
).launch(auth=('admin', '1234'))