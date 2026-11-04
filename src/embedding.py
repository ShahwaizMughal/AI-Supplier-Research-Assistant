from chromadb.utils.embedding_functions import DefaultEmbeddingFunction


def get_embedding_function():
    """
    Return ChromaDB's default embedding function.
    """

    return DefaultEmbeddingFunction()