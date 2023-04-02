from translate import Translator

translator = Translator(from_lang='Russian', to_lang='English')
result = translator.translate("кривой переводчик")

print(result)
