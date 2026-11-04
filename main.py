from src.agent import ask_agent


def main():

    print("=" * 55)
    print("       AI SUPPLIER RESEARCH ASSISTANT")
    print("=" * 55)

    print("\nAsk questions about your suppliers.")
    print("Type 'exit' to close the application.\n")

    while True:

        question = input("You: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("\nApplication closed.")
            break

        if not question:
            print("Please enter a question.\n")
            continue

        try:

            answer = ask_agent(question)

            print("\nAssistant:")
            print(answer)

        except Exception as error:

            print(f"\nError: {error}")

        print("\n" + "-" * 55 + "\n")


if __name__ == "__main__":
    main()