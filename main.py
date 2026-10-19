import requests

def get_ai_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    api_key = "YOUR_API_KEY"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "system", "content": "আপনি Tasnim Hassan AI। আপনি একজন অত্যন্ত বুদ্ধিমান ও বিনয়ী সহকারী।"},
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"এরর: {response.status_code}"
    except Exception as e:
        return f"সংযোগ সমস্যা: {e}"

def start_app():
    print("==========================================")
    print("   Tasnim Hassan Super AI Mobile App      ")
    print("==========================================")
    while True:
        user_input = input("\nTasnim Hassan: ").strip()
        if not user_input or user_input.lower() in ['exit', 'quit']:
            break
        print("Tasnim Hassan Super AI চিন্তা করছে...", end="\r")
        reply = get_ai_response(user_input)
        print(f"Tasnim Hassan Super AI: {reply}")

if __name__ == "__main__":
    start_app()
