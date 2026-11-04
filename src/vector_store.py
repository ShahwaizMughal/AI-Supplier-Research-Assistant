import chromadb

from src.embedding import get_embedding_function


CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "supplier_documents"


def get_chroma_client():
    """
    Create a persistent ChromaDB client.
    """

    return chromadb.PersistentClient(path=CHROMA_PATH)


def get_collection():
    """
    Get or create the supplier documents collection.
    """

    client = get_chroma_client()

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=get_embedding_function(),
        metadata={"description": "Supplier document knowledge base"}
    )

    return collection