from googletrans import Translator
translator = Translator()
text1 = "How are"
translated_text = translator.translate(text1, dest='en')
print(translated_text.text)
