from services.huggingface_service import summarize_text
from services.ollama_service import query_ollama

def handle_query(query, df):
    # Combine AI responses
    summary = summarize_text(df.to_string())
    ollama_response = query_ollama(query)
    return f"📊 Summary:\n{summary}\n\n🧠 Ollama:\n{ollama_response}"
