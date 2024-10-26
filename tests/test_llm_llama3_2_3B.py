import requests
import pytest

def get_ollama_version():
    """Get Ollama version"""
    try:
        response = requests.get("http://localhost:11434/api/version")
        return response.json()['version']
    except Exception as e:
        raise ConnectionError(f"Connection error: {e}")
def get_available_models():
    """Get all models available in Ollama"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        return response.json().get("models", [])
    except Exception as e:
        raise ConnectionError(f"Error listing models: {e}")

def generate_text(model_name, prompt):
    """Generate text with specified model"""
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=data
        )
        return response.json().get("response", "No response")
    except Exception as e:
        raise RuntimeError(f"Generation error: {e}")
def test_ollama_connection():
    """Test basic connectivity to Ollama"""
    version = get_ollama_version()
    assert version, "Failed to get Ollama version"
    print(f"Ollama version: {version}")
def test_list_available_models():
    """Test listing available models"""
    models = get_available_models()
    assert models, "No models available"
    print("\nAvailable models:")
    for model in models:
        print(f"- {model['name']}")

def test_generation():
    """Test basic generation with available model"""
    models = get_available_models()
    model_to_test = models[0]['name'] if models else "llama3.2"
    print(f"\nTesting generation with {model_to_test}...")
    response = generate_text(model_to_test, "What is artificial general intelligence?")
    assert response, "No response generated"
    print("\nTest response:")
    print(response)

if __name__ == "__main__":
    print("Testing Ollama setup...")
    try:
        test_ollama_connection()
        print("\nConnection successful!")
        test_list_available_models()
        test_generation()
    except Exception as e:
        print(f"\nTest failed: {e}")
