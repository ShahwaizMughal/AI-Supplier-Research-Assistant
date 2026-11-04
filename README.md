# AI Supplier Research Assistant

A Retrieval-Augmented Generation (RAG) application that uses Gemini, ChromaDB, and automatic tool calling to answer questions about supplier documents.

The project also exposes the AI agent through a FastAPI endpoint and supports Docker-based deployment.

## Features

- **Document ingestion:** Reads supplier documents from text files.
- **Text chunking:** Splits documents into smaller overlapping chunks.
- **Vector database:** Stores document embeddings in ChromaDB.
- **Semantic retrieval:** Retrieves relevant supplier information based on user queries.
- **RAG pipeline:** Provides retrieved document context to Gemini.
- **AI agent:** Uses Gemini automatic function calling.
- **Calculator tool:** Performs mathematical calculations.
- **Supplier search tool:** Searches the supplier knowledge base.
- **REST API:** Exposes the agent through FastAPI.
- **Request validation:** Uses Pydantic models.
- **Containerization:** Supports Docker and Docker Compose.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core development |
| Google Gemini | LLM and agent |
| Google GenAI SDK | Gemini integration |
| ChromaDB | Vector database |
| Built-in Chroma embedding function | Document and query embeddings |
| FastAPI | REST API |
| Pydantic | Request validation |
| Docker | Containerization |
| Pytest | Testing |

## Project Structure

```text
AI-Supplier-Research-Assistant/
│
├── data/
│   └── suppliers/
│       ├── supplier_1.txt
│       ├── supplier_2.txt
│       └── supplier_3.txt
│
├── chroma_db/
│
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── ingestion.py
│   ├── retrieval.py
│   ├── rag.py
│   ├── tools.py
│   └── vector_store.py
│
├── tests/
│   ├── __init__.py
│   └── test_queries.py
│
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── ingest.py
├── main.py
├── requirements.txt
└── README.md
```

The `chroma_db/` directory is generated automatically during document ingestion.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Supplier-Research-Assistant.git

cd AI-Supplier-Research-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash
```

Replace the API key placeholder with your actual Gemini API key.

## Usage

### 1. Ingest supplier documents

Run:

```bash
python ingest.py
```

This command:

1. Reads supplier text files.
2. Splits documents into overlapping chunks.
3. Generates embeddings through ChromaDB.
4. Stores documents and metadata in the persistent vector database.

### 2. Start the API server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 3. API documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides interactive API documentation through Swagger UI.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Health check |
| POST | `/ask` | Ask the AI assistant |

### Example Request

**POST `/ask`**

```json
{
    "question": "Which supplier has the lowest standard MOQ?"
}
```

### Example Response

```json
{
    "question": "Which supplier has the lowest standard MOQ?",
    "answer": "Precision Mechanical Works has the lowest standard MOQ of 100 units."
}
```

The answer is generated dynamically using the supplier documents stored in ChromaDB.

## Example Questions

You can ask questions such as:

- Which supplier has the lowest standard MOQ?
- Compare the lead times of all suppliers.
- Which supplier offers ISO 14001 certification?
- Which supplier is located in Lahore?
- What are the payment terms of Global Plastics Manufacturing?
- Which supplier provides CNC machined components?
- What would 500 units cost at $8 per unit?

The agent uses document search for supplier-related questions and the calculator tool for mathematical operations.

## Docker Deployment

### Build and run using Docker Compose

First, build the image and ingest the documents:

```bash
docker compose build
```

```bash
docker compose run --rm supplier-assistant python ingest.py
```

Then start the application:

```bash
docker compose up
```

The API will be available at:

```text
http://localhost:8000
```

To stop the application:

```bash
docker compose down
```

The ChromaDB data is persisted through a mounted volume.

## Running Tests

Run the test suite:

```bash
pytest
```

The included tests cover:

- Text chunking
- Empty document handling
- Chunk overlap
- Calculator addition
- Calculator multiplication
- Calculator division
- Invalid calculator expressions

These tests do not require Gemini API calls.

## Architecture

```text
                 Supplier Documents
                         |
                         v
                  Document Ingestion
                         |
                         v
                    Text Chunking
                         |
                         v
                   ChromaDB Storage
                         |
                         |
User Question            |
      |                  |
      v                  |
   FastAPI               |
      |                  |
      v                  |
  Gemini Agent <---------+
      |
      +------> Supplier Search Tool
      |
      +------> Calculator Tool
      |
      v
  Gemini Response
      |
      v
  API Response
```

## Current Project Scope

This project demonstrates:

- Retrieval-Augmented Generation
- Semantic search
- Vector databases
- LLM integration
- Automatic function calling
- Tool-based AI agents
- REST API development
- Docker containerization

## Limitations

- Supplier information is limited to the documents included in the knowledge base.
- The supplier records are sample data.
- Gemini requires a valid API key and available API quota.
- ChromaDB's default embedding model may need to be downloaded when first used.
- The application does not currently include user authentication or a frontend.

## Future Improvements

Possible future improvements include:

- Support for PDF and DOCX supplier documents.
- Improved document chunking and retrieval evaluation.
- More supplier comparison capabilities.
- Additional AI tools.
- Deployment to a cloud hosting platform.

## Author

**Shahwaiz Akram**

Computer Engineering Student


