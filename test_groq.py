import requests

url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "YOUR_GROQ_API_KEY"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {"role": "user", "content": "বাংলাদেশের রাজধানী কোথায়?"}
    ]
}

try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        res_json = response.json()
        print("\n==========================================")
        print("AI এর উত্তর:", res_json['choices'][0]['message']['content'])
        print("==========================================\n")
    else:
        print("\nAPI Error Code:", response.status_code)
        print("Details:", response.text)
except Exception as e:
    print("\nError:", e)
