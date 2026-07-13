from google import genai
from dotenv import load_dotenv
import os
from rag import similarity_search
import time
from google.genai import errors

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(question):
    docs=similarity_search(question)
    context="\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
    You are a Telecom RAG Assistant.

    Instructions:
    - Answer only using the provided context.
    - Do not make up information.
    - If the answer is not present, clearly state that.
    - Explain in simple technical language.
    - Summarize information from multiple context passages if needed.

    Context:
    {context}

    User Question:
    {question}

    Answer:
    """

    for attempt in range(5):
        try:
            response=client.models.generate_content(model='models/gemini-flash-latest',contents=prompt)
            return response.text,docs
        except errors.ServerError:
            if attempt<4:
                time.sleep(5)
            else:
                return("Currently experiencing high demand. Please try again in a minute.",docs)
        except Exception as e:
            return f"API error: {e}",docs