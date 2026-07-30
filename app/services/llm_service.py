from google import genai

from app.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
)

client = genai.Client(
    api_key=GOOGLE_API_KEY
)


def generate_response(question: str, context: str) -> str:

    prompt = f"""
You are an AI Knowledge Assistant.

Use ONLY the information provided in the context below.

Rules:
1. Give a direct and natural answer.
2. Do NOT say "Based on the provided context."
3. Do NOT mention the context.
4. Keep the answer clear and concise.
5. If the answer is not found in the context, reply exactly:
"I couldn't find this information in the knowledge base."

------------------------
Context:
{context}
------------------------

Question:
{question}

Answer:
"""

    try:

        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
        )

        if response.text:
            return response.text

        return "No response generated."

    except Exception as e:

        return f"Error generating response: {str(e)}"