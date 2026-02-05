INTENT_SUGGESTION_TOOL = {
    "type": "function",
    "function": {
        "name": "suggest_sentences",
        "description": "Convert fragmented text into clear sentence suggestions",
        "parameters": {
            "type": "object",
            "properties": {
                "intent": {
                    "type": "string",
                    "description": "High-level intent such as pain_report, need_help, emotion, request"
                },
                "suggestions": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "minItems": 2,
                    "maxItems": 3
                }
            },
            "required": ["intent", "suggestions"]
        }
    }
}
