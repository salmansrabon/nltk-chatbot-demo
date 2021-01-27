from googletrans import Translator
#pip install googletrans==3.1.0a0

def translateToEnglish(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    # print(translation.text)
    return translation.text

def translateToBangla(text):
    translator = Translator()
    translation = translator.translate(text, dest='bn')
    return translation.text

res=translateToBangla("How are you")
print(res)