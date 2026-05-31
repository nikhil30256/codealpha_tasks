from deep_translator import GoogleTranslator

print("Language Translation Tool")

text = input("Enter text: ")
source_lang = input("Source language (e.g. en): ")
target_lang = input("Target language (e.g. hi): ")

translated = GoogleTranslator(
    source=source_lang,
    target=target_lang
).translate(text)

print("\nTranslated Text:")
print(translated)
