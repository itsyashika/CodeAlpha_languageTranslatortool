# simple_translator.py
# Easy Language Translator Project using Python Dictionary

translations = {
    "hello": {
        "hindi": "नमस्ते",
        "french": "bonjour",
        "spanish": "hola"
    },
    "thank you": {
        "hindi": "धन्यवाद",
        "french": "merci",
        "spanish": "gracias"
    },
    "good morning": {
        "hindi": "सुप्रभात",
        "french": "bonjour",
        "spanish": "buenos días"
    },
    "bye": {
        "hindi": "अलविदा",
        "french": "au revoir",
        "spanish": "adiós"
    }
}

print("=== Simple Language Translator ===")
print("Available languages: hindi, french, spanish")

word = input("Enter English word/sentence: ").lower()
language = input("Translate to: ").lower()

if word in translations and language in translations[word]:
    print("Translated Text:", translations[word][language])
else:
    print("Sorry, translation not available.")