import gradio as gr
from core.prompts.system_prompts import SYSTEM_PROMPT
from services.llm_client import LLMClient
from core.tools.intent_suggest import INTENT_SUGGESTION_TOOL
from utils.logger import get_logger

logger = get_logger(__name__)

model = "gpt-4.1-mini"
llm = LLMClient(model=model)

def chat(message, history):
    logger.info(f"User message received: {message}")

    try:
        result = llm.suggest_sentences(
            system_prompt=SYSTEM_PROMPT,
            user_input=message,
            tool_schema=INTENT_SUGGESTION_TOOL
        )
        logger.info(result)
        print(result)
        intent = result["intent"]
        suggestions = result["suggestions"]

        logger.info(f"Inferred intent: {intent}")
        logger.info(f"Suggestions generated: {suggestions}")

        formatted_response = "Suggested messages:\n\n"
        for idx, s in enumerate(suggestions, start=1):
            formatted_response += f"{idx}. {s}\n"

        return formatted_response

    except Exception as e:
        logger.exception("Sprint 1 generation failed")
        return "Sorry. I could not generate suggestions right now."


gr.ChatInterface(
    fn=chat,
    title="Aphasia Assist",
    flagging_mode="never"
).launch(inbrowser=True)