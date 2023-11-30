from image_recognition import image_recognition
from text_generation import text_generation

def recognize_and_generate_text(image_url, prompt, text_model_name, system_message, user_message_template):
    # 画像認識を行い、結果を取得
    recognition_result = image_recognition.recognize_image(image_url, prompt)
    print(f"Recognition result: {recognition_result.message.content}")

    # ユーザーメッセージの作成
    user_message = user_message_template.format(recognition_result.message.content)

    # テキストを生成する
    generated_text = text_generation.generate_text(text_model_name, system_message, user_message)
    return generated_text

if __name__ == "__main__":
    # 画像認識のパラメータ
    image_url = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2627015/ee531ce6-6e85-4cbd-66e4-4fcb5870af4c.png"
    recognition_prompt = "ポケモンのタイプを分類して"

    # テキスト生成のパラメータ
    text_model_name = "gpt-4"
    system_message = "あなたはポケモンバトルの専門家です。"
    user_message_template = "下記の特徴を持つポケモンの弱点を見つけてください。\n{}"

    # 画像認識とテキスト生成を行う
    generated_text = recognize_and_generate_text(
        image_url, recognition_prompt, text_model_name, system_message, user_message_template
    )

    print(generated_text)
