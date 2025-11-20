import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_AI(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3,
        max_tokens=300,
    )
    return response["choices"][0]["message"]["content"].strip()


def ask_ai_for_feedback(question, correct_answer, student_answer):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an astronomy tutor. "
                "If the student is correct, respond ONLY with: CORRECT_ANSWER. "
                "If wrong, give a helpful short hint without revealing the answer. Give a hint without saying hint."
            )
        },
        {
            "role": "user",
            "content": f"""
            Question: {question}
            Correct answer: {correct_answer}
            Student answer: {student_answer}
            """
        }
    ]
    return query_AI(messages)


def ask_the_bot(prompt):
    messages = [
        {"role": "system", "content": "You help astronomy students answer questions simply."},
        {"role": "user", "content": prompt}
    ]
    return query_AI(messages)