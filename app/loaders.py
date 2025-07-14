
import csv
from langchain.docstore.document import Document
from pathlib import Path

def load_faq_csv(csv_path: str | Path) -> list[Document]:
    documents = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            content = f"Q: {row['question']}\nA: {row['answer']}"
            metadata = {
                "category": row["category"],
                "source": row["source"]
            }
            documents.append(Document(page_content=content, metadata=metadata))
    return documents
