"""Command-line chatbot for querying the Instrumento AGU PDF."""

from __future__ import annotations

import argparse
from pathlib import Path

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


class ContractChatbot:
    """Simple wrapper around LangChain RetrievalQA pipeline."""

    def __init__(self, pdf_path: str | Path) -> None:
        pdf = Path(pdf_path)
        if not pdf.exists():
            raise FileNotFoundError(pdf)

        loader = PyPDFLoader(str(pdf))
        pages = loader.load_and_split()

        embeddings = HuggingFaceEmbeddings()
        vectordb = Chroma.from_documents(pages, embeddings)

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        self.qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectordb.as_retriever())

    def ask(self, question: str) -> str:
        """Return the answer for *question* using the QA chain."""
        result = self.qa({"query": question})
        return result["result"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the Instrumento AGU PDF")
    parser.add_argument(
        "--pdf",
        default="inputs/Instrumento_AGU.pdf",
        help="Path to the Instrumento AGU PDF",
    )
    args = parser.parse_args()

    bot = ContractChatbot(args.pdf)
    print("Digite sua pergunta (ou 'sair' para finalizar):")

    while True:
        query = input("\n> ")
        if query.lower() in {"sair", "exit", "quit"}:
            break
        answer = bot.ask(query)
        print(f"\nResposta:\n{answer}\n")


if __name__ == "__main__":
    main()
