from image_recognition import image_recognition
from image_generation import image_generation

def recognize_and_generate_image(image_url, recognition_prompt, model_name):
    # 画像認識を行い、結果を取得
    recognition_result = image_recognition.recognize_image(image_url, recognition_prompt)
    print(f"Recognition result: {recognition_result.message.content}")

    # 生成する画像のプロンプトを設定
    generation_prompt = recognition_result.message.content

    # 画像を生成
    generated_image_response = image_generation.generate_image(model_name, generation_prompt)
    print(generated_image_response)

    return generated_image_response

if __name__ == "__main__":
    # 画像認識と画像生成のパラメータ設定
    image_url = "https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2627015/ee531ce6-6e85-4cbd-66e4-4fcb5870af4c.png"
    recognition_prompt = "ポケモンの特徴をなるべく詳しく分析し、その対となるポケモンを生成するプロンプトを教えてください"
    model_name = "dall-e-3"

    # 画像認識と画像生成の処理を実行
    response = recognize_and_generate_image(image_url, recognition_prompt, model_name)
    print(response)
