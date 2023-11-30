from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "一人称が「オラ」で、口癖は「ワクワクすっぞ！」です。"},
    {"role": "user", "content": "明日の天下一武道会の意気込みをお願いします！"}
  ]
)

print(completion.choices[0].message)
