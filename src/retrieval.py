from src.vector_store import get_collection


def retrieve(query, top_k=3, max_distance=1.5):

    collection = get_collection()

    if collection.count() == 0:
        return []

    results = collection.query(
        query_texts=[query],
        n_results=min(top_k, collection.count())
    )

    retrieved_documents = []

    ids = results["ids"][0]
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for index in range(len(ids)):

        distance = distances[index]

        if distance > max_distance:
            continue

        retrieved_documents.append({
            "source": metadatas[index]["source"],
            "chunk_id": metadatas[index]["chunk_id"],
            "distance": distance,
            "text": documents[index]
        })

    return retrieved_documents