from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Think of a short-form video idea for a social media platform. The video should be funny and engaging, and should be less than 30 seconds long, it should be satire and should not be personal. Write the title under Title: and the description under Description:"},
  ]
)

print(response.choices[0].message.content)