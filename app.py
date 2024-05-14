import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate

# Configurar credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "caminho_para_suas_credenciais.json"

# Função para transcrever voz para texto
def transcrever_audio(audio_file):
    client = speech.SpeechClient()
    with open(audio_file, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="pt-BR"
    )
    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        return result.alternatives[0].transcript

# Função para traduzir texto para o idioma desejado
def traduzir_texto(texto, idioma_destino):
    client = translate.Client()
    return client.translate(texto, target_language=idioma_destino)

# Função principal
def main():
    # Nome do arquivo de áudio a ser transcritp
    audio_file = "exemplo.wav"
    
    # Transcrever áudio para texto
    texto_transcrito = transcrever_audio(audio_file)
    print("Texto transcrito:", texto_transcrito)
    
    # Traduzir texto para o idioma desejado
    idioma_destino = "en"  # Idioma desejado (exemplo: inglês)
    texto_traduzido = traduzir_texto(texto_transcrito, idioma_destino)
    print("Texto traduzido:", texto_traduzido)

if __name__ == "__main__":
    main()
