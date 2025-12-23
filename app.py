from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from src.prompt import system_prompt

from groq import Groq


# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------

load_dotenv()

app = Flask(__name__, template_folder="templates")

pinecone_api_key = os.getenv("PINECONE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = pinecone_api_key

print(" Environment variables loaded")


# ---------------------------------------------------
# Groq Client (UPDATED MODELS)
# ---------------------------------------------------

client = Groq(api_key=groq_api_key)
print(" Groq client initialized")


# ---------------------------------------------------
# RAG Globals
# ---------------------------------------------------

embeddings = None
retriever = None
use_rag = False


def init_rag():
    global embeddings, retriever, use_rag

    if retriever:
        return

    print(" Initializing RAG...")

    embeddings = download_embeddings()

    docsearch = PineconeVectorStore(
        embedding=embeddings,
        index_name="medical-chatbot-index"
    )

    retriever = docsearch.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    use_rag = True
    print(" RAG initialized successfully")


# ---------------------------------------------------
# Routes
# ---------------------------------------------------

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form.get("msg", "").strip()
    print(f" User Input: {user_input}")

    if not user_input:
        return "Please enter a valid medical question."

    if not use_rag:
        init_rag()

    # ---------------------------------------------------
    # Retrieve context from Pinecone
    # ---------------------------------------------------

    context = ""
    if retriever:
        docs = retriever.invoke(user_input)
        context = "\n\n".join(d.page_content for d in docs[:5])
        print(f" Retrieved {len(docs)} documents")

    # ---------------------------------------------------
    # Prompt
    # ---------------------------------------------------

    system_message = system_prompt.format(context=context)

    # ---------------------------------------------------
    # Groq Chat Completion (FIXED MODEL NAME)
    # ---------------------------------------------------

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ ACTIVE MODEL
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=300
        )

        answer = response.choices[0].message.content.strip()

    except Exception as e:
        print(" Groq error:", e)
        answer = "The AI model is temporarily unavailable. Please try again."

    print(f" Response: {answer}")
    return answer


# ---------------------------------------------------
# Run App
# ---------------------------------------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
