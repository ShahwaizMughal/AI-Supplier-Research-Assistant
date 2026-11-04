import ast
import operator
import json

from src.retrieval import retrieve


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


def evaluate_expression(node):
    """
    Safely evaluate supported arithmetic AST nodes.
    """

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return node.value

        raise ValueError("Only numeric values are allowed.")

    if isinstance(node, ast.BinOp):
        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported mathematical operation.")

        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 10:
            raise ValueError("Exponent is too large.")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported unary operation.")

        return operation(evaluate_expression(node.operand))

    raise ValueError("Invalid mathematical expression.")


def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Args:
        expression: A basic arithmetic expression.

    Returns:
        The calculation result.
    """

    try:
        parsed_expression = ast.parse(
            expression,
            mode="eval"
        )

        result = evaluate_expression(parsed_expression.body)

        return str(result)

    except Exception as error:
        return f"Calculation error: {str(error)}"


def create_search_tool(collection):
    """
    Create a supplier document search tool connected
    to the provided ChromaDB collection.
    """

    def search_supplier_documents(query: str) -> str:
        """
        Search supplier documents for relevant information.

        Args:
            query: Supplier-related information to search for.

        Returns:
            Relevant supplier document chunks.
        """

        try:

            if collection.count() == 0:
                return "The supplier knowledge base is empty."

            results = collection.query(
                query_texts=[query],
                n_results=min(3, collection.count())
            )

            retrieved_documents = []

            ids = results["ids"][0]
            documents = results["documents"][0]
            metadatas = results["metadatas"][0]
            distances = results["distances"][0]

            for index in range(len(ids)):

                distance = distances[index]

                if distance > 1.0:
                    continue

                retrieved_documents.append({
                    "source": metadatas[index]["source"],
                    "chunk_id": metadatas[index]["chunk_id"],
                    "distance": distance,
                    "text": documents[index]
                })

            if not retrieved_documents:
                return "No relevant supplier information was found."

            return json.dumps(
                retrieved_documents,
                indent=2,
                ensure_ascii=False
            )

        except Exception as error:
            return f"Document search error: {str(error)}"

    return search_supplier_documents