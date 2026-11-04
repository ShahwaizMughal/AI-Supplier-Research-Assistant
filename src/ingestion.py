from pathlib import Path

from src.chunking import split_text
from src.vector_store import get_collection


DATA_DIRECTORY = Path("data/suppliers")


def ingest_documents():
    """
    Load supplier documents and store their chunks in ChromaDB.
    """

    collection = get_collection()

    if not DATA_DIRECTORY.exists():
        raise FileNotFoundError(
            f"Supplier directory not found: {DATA_DIRECTORY}"
        )

    document_files = list(DATA_DIRECTORY.glob("*.txt"))

    if not document_files:
        raise FileNotFoundError(
            "No supplier text files found in data/suppliers."
        )

    all_ids = []
    all_documents = []
    all_metadatas = []

    for file_path in document_files:

        print(f"Processing: {file_path.name}")

        text = file_path.read_text(encoding="utf-8")

        chunks = split_text(
            text,
            chunk_size=300,
            overlap=50
        )

        for index, chunk in enumerate(chunks):

            chunk_id = f"{file_path.stem}_{index}"

            all_ids.append(chunk_id)
            all_documents.append(chunk)

            all_metadatas.append({
                "source": file_path.name,
                "chunk_id": index
            })

    collection.upsert(
        ids=all_ids,
        documents=all_documents,
        metadatas=all_metadatas
    )

    print("\nIngestion completed successfully!")
    print(f"Documents processed: {len(document_files)}")
    print(f"Chunks stored: {len(all_documents)}")
    print(f"Collection count: {collection.count()}")

    return collection.count()