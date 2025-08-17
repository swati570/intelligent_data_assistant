import subprocess

def query_ollama(prompt):
    result = subprocess.run(["ollama", "run", "llama2", prompt], capture_output=True, text=True)
    return result.stdout
