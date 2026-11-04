from src.retrieval import retrieve


def get_relevant_context(query):
    """
    Retrieve relevant supplier information
    and combine it into a context string.
    """

    results = retrieve(
        query=query,
        top_k=3,
        max_distance=1.0
    )

    if not results:
        return "", []

    context_parts = []

    for result in results:

        context_parts.append(
            f"Source: {result['source']}\n"
            f"Information: {result['text']}"
        )

    context = "\n\n".join(context_parts)

    return context, results