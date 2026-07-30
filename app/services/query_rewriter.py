from google import genai

from app.config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)


def rewrite_question(question: str, history: str) -> str:

    prompt = f"""
You are a query rewriting assistant.

Your task is to rewrite the user's latest question into a complete, standalone question using the conversation history.

Rules:
1. Replace pronouns like it, they, this, that, he, she with the correct subject.
2. Keep the meaning exactly the same.
3. Do not answer the question.
4. Return ONLY the rewritten question.
5. If the question is already complete, return it unchanged.

Conversation History:
{history}

Current Question:
{question}

Rewritten Question:
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text.strip()

if __name__ == "__main__":

    history = """
User: What is FastAPI?
Assistant: FastAPI is a Python web framework.
"""

    question = "Who created it?"

    print(rewrite_question(question, history))