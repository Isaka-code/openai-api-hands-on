from openai import OpenAI

def recognize_image(image_url, prompt):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url},
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0]

if __name__ == "__main__":
    image_url = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2627015/5a1a7f3f-851b-4673-d6e5-d3ad51621be7.png"
    prompt="柿ピーを数えて"

    result = recognize_image(image_url, prompt)

    print(result)
