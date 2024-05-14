import os
import tkinter as tk
from tkinter import filedialog
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

# Função para selecionar arquivo de áudio
def selecionar_arquivo():
    arquivo_selecionado = filedialog.askopenfilename(title="Selecione um arquivo de áudio")
    if arquivo_selecionado:
        texto_transcrito = transcrever_audio(arquivo_selecionado)
        texto_traduzido = traduzir_texto(texto_transcrito, "en")  # Traduzir para inglês por padrão
        texto_transcrito_label.config(text="Texto transcrito:\n" + texto_transcrito)
        texto_traduzido_label.config(text="Texto traduzido:\n" + texto_traduzido)

# Criar janela principal
root = tk.Tk()
root.title("Conversor de Voz para Texto e Tradução")

# Botão para selecionar arquivo de áudio
selecionar_arquivo_button = tk.Button(root, text="Selecionar Arquivo de Áudio", command=selecionar_arquivo)
selecionar_arquivo_button.pack(pady=10)

# Labels para exibir texto transcrito e traduzido
texto_transcrito_label = tk.Label(root, text="Texto transcrito:\n")
texto_transcrito_label.pack(pady=5)

texto_traduzido_label = tk.Label(root, text="Texto traduzido:\n")
texto_traduzido_label.pack(pady=5)

# Rodar aplicativo
root.mainloop()
