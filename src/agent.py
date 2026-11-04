import os

from google import genai
from google.genai import types
from dotenv import load_dotenv

from src.tools import calculator, create_search_tool
from src.vector_store import get_collection


load_dotenv()


SYSTEM_INSTRUCTION = """
You are an AI Supplier Research Assistant.

Your job is to answer questions about the suppliers
stored in the supplier document knowledge base.

Rules:

1. Use the search_supplier_documents tool for supplier-related questions.
2. Use the calculator tool when mathematical calculations are required.
3. Do not invent supplier information.
4. Base supplier-related answers on retrieved documents.
5. If the required information is unavailable, clearly say so.
6. Use actual supplier names instead of referring to suppliers
   only by numbers.
7. When comparing suppliers, explain the comparison clearly.
8. When calculating costs, show the calculation.
9. Do not assume that missing information is available.
"""


def get_gemini_client():
    """
    Initialize the Gemini client.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Add it to your .env file."
        )

    return genai.Client(api_key=api_key)


def ask_agent(question):
    """
    Send a question to the Gemini agent.

    Gemini can automatically call the available tools
    when additional information or calculations are needed.
    """

    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    model_name = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.6-flash"
    )

    client = get_gemini_client()

    collection = get_collection()

    search_supplier_documents = create_search_tool(collection)

    tools = [
        calculator,
        search_supplier_documents
    ]

    response = client.models.generate_content(
        model=model_name,
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            tools=tools,
            temperature=0.2
        )
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text