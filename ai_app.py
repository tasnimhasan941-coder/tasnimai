import os
import requests

def get_ai_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    api_key = "YOUR_GROQ_API_KEY"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "system",
                "content": "আপনি Tasnim Hassan AI। আপনি একজন অত্যন্ত বুদ্ধিমান সহকারী।"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"API এরর ({response.status_code}): {response.text}"
    except Exception as e:
        return f"সংযোজন সমস্যা: {e}"

def ai_chat_app():
    user_name = "Tasnim Hassan"
    bot_name = f"{user_name} Super AI"
    
    print("==========================================")
    print(f"      স্বাগতম! {bot_name}-এ      ")
    print("==========================================")

    while True:
        user_input = input(f"\n{user_name}: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ['exit', 'quit', 'বন্ধ']:
            print(f"\nAI: ধন্যবাদ {user_name}! আবার কথা হবে।")
            break

        print(f"{bot_name} চিন্তা করছে...", end="\r")
        reply = get_ai_response(user_input)
        print(f"{bot_name}: {reply}")

if __name__ == "__main__":
    ai_chat_app()
