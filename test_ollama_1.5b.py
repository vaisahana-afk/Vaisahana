import json
import requests

# Set up the payload for Ollama's local API
url = "http://localhost:11434/api/generate"
payload = {
    "model": "qwen2.5-coder:1.5b",
    "prompt": "Write a Python FastAPI endpoint for fraud detection.",
    "stream": True  # Switched to True for real-time text delivery
}

print("Sending prompt to local Ollama (1.5b)... Streaming response below: 👇\n")

try:
    # Make the POST request with stream=True
    response = requests.post(url, json=payload, stream=True)

    if response.status_code == 200:
        # Read the incoming chunks line by line as they arrive
        for line in response.iter_lines():
            if line:
                # Parse each piece of text and print it immediately
                chunk = json.loads(line.decode('utf-8'))
                print(chunk.get("response", ""), end="", flush=True)
        print("\n")  # Add a clean new line at the end
    else:
        print(f"\nError: Server responded with status code {response.status_code}")

except requests.exceptions.ConnectionError:
    print("\nError: Could not connect to Ollama. Make sure the server is running!")
