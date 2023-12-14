# ChatGoogleGenerativeAI
import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass("Provide your Google API Key")

# Example usage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("Write a ballad about LangChain")
print(result.content)

# Streaming and Batching
for chunk in llm.stream("Write a limerick about LLMs."):
    print(chunk.content)
    print("---")
# Note that each chunk may contain more than one "token"

results = llm.batch(
    [
        "What's 2+2?",
        "What's 3+5?",
    ]
)
for res in results:
    print(res.content)


# Multimodal support

# (Jupyter Notebook)
# import requests
# from IPython.display import Image

# image_url = "https://picsum.photos/seed/picsum/300/300"
# content = requests.get(image_url).content
# Image(content)



# (Python Script)
from io import BytesIO

import requests
from PIL import Image

image_url = "https://picsum.photos/seed/picsum/300/300"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
image.save('image.png')
image.show()


from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
# example
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "What's in this image?",
        },  # You can optionally provide text parts
        {"type": "image_url", "image_url": image_url},
    ]
)
print(llm.invoke([message]))
