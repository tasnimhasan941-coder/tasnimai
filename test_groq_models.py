import requests

api_key = "YOUR_GROQ_API_KEY"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# ১. বর্তমানে আপনার API Key দিয়ে অ্যাক্সেসযোগ্য মডেলের লিস্ট বের করা
models_url = "https://api.groq.com/openai/v1/models"
try:
    m_resp = requests.get(models_url, headers=headers)
    if m_resp.status_code == 200:
        models_data = m_resp.json().get('data', [])
        available_models = [m['id'] for m in models_data]
        print("স্বাগতম! আপনার অ্যাকাউন্টে সচল মডেলসমূহ:")
        for mod in available_models[:5]:
            print(" -", mod)
        
        # সচল যেকোনো একটি প্রধান মডেল বেছে নেওয়া
        chosen_model = available_models[0] if available_models else "openai/gpt-oss-20b"
        print(f"\n[+] আমরা ব্যবহার করছি: {chosen_model}")

        # ২. সেই সচল মডেল দিয়ে চ্যাট রিকোয়েস্ট পাঠানো
        chat_url = "https://api.groq.com/openai/v1/chat/completions"
        payload = {
            "model": chosen_model,
            "messages": [
                {"role": "user", "content": "বাংলাদেশের রাজধানী কোথায়?"}
            ]
        }
        
        c_resp = requests.post(chat_url, json=payload, headers=headers)
        if c_resp.status_code == 200:
            ans = c_resp.json()['choices'][0]['message']['content']
            print("\n==========================================")
            print("AI এর উত্তর:", ans)
            print("==========================================\n")
        else:
            print("\nChat API Error:", c_resp.status_code, c_resp.text)
    else:
        print("\nModels Fetch Error:", m_resp.status_code, m_resp.text)

except Exception as e:
    print("\nError:", e)
