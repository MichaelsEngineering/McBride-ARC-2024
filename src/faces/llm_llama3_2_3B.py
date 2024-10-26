import requests

def generate_llama_response(prompt, model_name="llama3.2"):
    """
    Generate a response from LLaMA using Ollama's API
    
    Args:
        prompt (str): The input prompt
        model_name (str): Name of the model to use (default: "llama3.2")
        
    Returns:
        str: The generated response
    """
    API_URL = "http://localhost:11434/api/generate"
    
    # Prepare the request
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False  # Get complete response rather than streaming
    }
    
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return None

def format_chat_messages(messages):
    """
    Format a list of chat messages into a single prompt string
    
    Args:
        messages (list): List of message dictionaries with 'role' and 'content'
        
    Returns:
        str: Formatted prompt string
    """
    formatted_prompt = ""
    for message in messages:
        role = message["role"]
        content = message["content"]
        
        if role == "system":
            formatted_prompt += f"System: {content}\n\n"
        elif role == "user":
            formatted_prompt += f"User: {content}\n"
        elif role == "assistant":
            formatted_prompt += f"Assistant: {content}\n"
            
    return formatted_prompt

def run_test_prompt():
    """
    Run a test prompt and print the response
    """
    messages = [
        {
            "role": "system",
            "content": "You are an https://arcprize.org/guide expert",
        },
        {
            "role": "user",
            "content": "Who is Francois Chollet?",
        },
    ]
    
    # Format the messages into a prompt
    prompt = format_chat_messages(messages)
    print("\nSending prompt to LLaMA:")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    
    # Generate response
    response = generate_llama_response(prompt)
    
    if response:
        print("\nLLaMA Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)
        return response
    else:
        print("No response received from LLaMA")
        return None

# Example usage
if __name__ == "__main__":
    print("Testing LLaMA interface...")
    run_test_prompt()