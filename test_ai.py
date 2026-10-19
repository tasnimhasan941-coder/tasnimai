import requests

def main():
    url = "https://api.groq.com/openai/v1/chat/completions"
    api_key = "YOUR_API_KEY"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "আপনি Tasnim Hassan AI। বিনয়ীভাবে উত্তর দিন।"},
            {"role": "user", "content": "বাংলাদেশের রাজধানী কোথায়?"}
        ]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("\nAI এর উত্তর:", response.json()['choices'][0]['message']['content'])
        else:
            print("\nAPI Error:", response.status_code, response.text)
    except Exception as e:
        print("\nException:", e)

if __name__ == "__main__":
    main()
