from text_generation import text_generation
from image_generation import image_generation

def text_and_image_generation(model_name, system_message, user_message, image_model):
    # テキストを生成する
    generated_text = text_generation.generate_text(model_name, system_message, user_message)
    print("Generated text:", generated_text)

    # 生成したテキストを基に画像を生成する
    response = image_generation.generate_image(image_model, generated_text)
    print("Generated image response:", response)

if __name__ == "__main__":
    # テキスト生成のパラメータ
    text_model_name = "gpt-4"
    system_message = "あなたはポケモンの専門家で、新しいポケモンのアイデアを提案するのが得意です。"
    user_message = "新しい1匹のポケモンを生成するプロンプトを考えてください"

    # 画像生成のパラメータ
    image_model = "dall-e-3"

    # テキストと画像の生成を行う
    text_and_image_generation(text_model_name, system_message, user_message, image_model)
