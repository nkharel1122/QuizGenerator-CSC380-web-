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
                "You are an astronomy quiz grader. "
                "You must be VERY strict. "
                "ONLY respond with CORRECT_ANSWER if the student's answer directly matches the correct answer "
                "or is an unambiguous synonym with the SAME meaning. "
                "Do NOT mark vague responses such as 'yes', 'okay', 'I agree', or partial ideas as correct. "
                "If the student answer is incorrect, respond with a hint without saying 'hint'. "
                "Do NOT reveal the correct answer, unless the student specifically asks for the answer"
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