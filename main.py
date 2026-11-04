from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.agent import ask_agent


app = FastAPI(
    title="AI Supplier Research Assistant",
    description="A RAG-based AI assistant for supplier research and comparison.",
    version="1.0.0"
)


class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Question about the available suppliers."
    )


class AskResponse(BaseModel):
    answer: str


@app.get("/")
def home():
    return {
        "message": "AI Supplier Research Assistant API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    try:
        answer = ask_agent(request.question)

        return AskResponse(answer=answer)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        print(f"ERROR TYPE: {type(error).__name__}")
        print(f"ERROR DETAILS: {error}")

        error_message = str(error)

        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            raise HTTPException(
                status_code=503,
                detail="The AI service is temporarily unavailable due to its usage quota. Please try again later."
            )

        raise HTTPException(
            status_code=500,
            detail="An internal error occurred while processing your question."
        )