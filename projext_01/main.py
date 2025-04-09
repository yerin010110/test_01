from dotenv import load_dotenv
import os
import openai

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "테스트"}]
)

print("전체 응답 구조 확인:", response)
print("출력 메시지:", response.choices[0].message.content)




