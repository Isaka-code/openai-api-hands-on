from text_generation import text_generation
from text_to_speech import text_to_speech


def main(model_name, system_message, user_message):
    # 英文から問題のテキストを生成する
    generated_text = text_generation.generate_text(model_name, system_message, user_message)
    print(generated_text)

    # 問題文を読み上げる音声合成
    text_to_speech.text_to_speech(generated_text)


if __name__ == "__main__":
    # テキスト生成のパラメータ
    text_model_name = "gpt-4"
    system_message = "Create a TOEIC-style multiple choice question (with options A, B, and C) based on the following English text. Also, provide the correct answer."
    user_message = """
                ---

                **Introduction:**
                This year, I've taken up the challenge of a solo AdCalendar initiative, choosing generative AI as my central theme. In this article, I aim to outline my preparations for this endeavor in a Q&A format. Hopefully, this will be beneficial to anyone contemplating their own AdCalendar challenge, whether going solo or not. Let’s dive in together!

                **Summary of Preparations for a Solo AdCalendar in Q&A Format**

                - **Q1: What motivated you to undertake a solo AdCalendar?**
                **A:** My primary objective is to win a Qiitan stuffed animal.

                - **Q2: Why did you choose to focus on generative AI?**
                **A:** This year has seen significant advancements in generative AI. The vast amount of new information, which I believe has overwhelmed most people, spurred me to increase my creative output. I decided to zero in on this single topic, convinced that working within certain boundaries would enhance my creativity.

                ---
                """

    main(text_model_name, system_message, user_message)

