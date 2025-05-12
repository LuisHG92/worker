import requests
import time

# Ejemplo estático, puedes integrarlo luego con colas, BD, etc.
TEXT_TO_TRANSLATE = "Hello, how are you?"

def translate(text, source="en", target="es"):
    response = requests.post(
        "https://libretranslate.com/translate",
        data={
            "q": text,
            "source": source,
            "target": target,
            "format": "text"
        }
    )
    return response.json()['translatedText']

if __name__ == "__main__":
    print("Worker de traducción iniciado...")
    while True:
        translated = translate(TEXT_TO_TRANSLATE)
        print(f"Traducido: {translated}")
        time.sleep(10)  # Simula esperar otro texto cada 10s
