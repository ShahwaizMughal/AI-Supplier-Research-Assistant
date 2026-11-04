from src.chunking import split_text
from src.tools import calculator


def test_chunking_returns_chunks():

    text = "A" * 700

    chunks = split_text(
        text,
        chunk_size=300,
        overlap=50
    )

    assert len(chunks) > 1


def test_chunking_empty_text():

    chunks = split_text("")

    assert chunks == []


def test_chunking_overlap():

    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 20

    chunks = split_text(
        text,
        chunk_size=100,
        overlap=20
    )

    assert chunks[0][-20:] == chunks[1][:20]


def test_calculator_addition():

    result = calculator("25 + 15")

    assert result == "40"


def test_calculator_multiplication():

    result = calculator("25 * 4")

    assert result == "100"


def test_calculator_division():

    result = calculator("100 / 4")

    assert result == "25.0"


def test_calculator_rejects_invalid_expression():

    result = calculator("import os")

    assert result.startswith("Calculation error:")