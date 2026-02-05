import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.logger import get_logger
from utils.exceptions import LLMError

load_dotenv()
logger = get_logger(__name__)

class LLMClient:
    def __init__(self, model: str):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            logger.error("OPENAI_API_KEY not found in environment variables")
            raise LLMError("Missing OPENAI_API_KEY")
        
        try:
            if api_key.startswith('sk-proj'):
                self.client = OpenAI(api_key=api_key)
                self.model = model
        except Exception as e:
            logger.exception("Invalid or API Key not found")
            raise LLMError(str(e))

    def stream_chat(self, messages):
        try:
            logger.info("Sending request to LLM")
            return self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=True
            )
        except Exception as e:
            logger.exception("LLM call failed")
            raise LLMError(str(e))
        
    def suggest_sentences(self, system_prompt, user_input, tool_schema):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=[tool_schema],
            tool_choice={"type": "function", "function": {"name": "suggest_sentences"}}
        )

        tool_args = response.choices[0].message.tool_calls[0].function.arguments
        parsed_args = json.loads(tool_args)
        return parsed_args
