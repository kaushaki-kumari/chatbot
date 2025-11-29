import anthropic
import os

anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL", "exm@gmail.com")

def generate_answer(question, context):
    try:
        msg = anthropic_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=800,
            messages=[{
                "role": "user",
                "content": f"""Answer based only on the following context:

{context}

Question: {question}

If you don’t know, say exactly:
"Sorry, I don't have this information. Please conatct {SUPPORT_EMAIL} for assitance."
"""
            }]
        )
        return msg.content[0].text
    except Exception as e:
        return f"(Error generating answer) {e}"
