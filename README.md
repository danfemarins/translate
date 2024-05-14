# Conversor de Voz para Texto e Tradução de Texto

Este é um projeto simples que demonstra como converter voz para texto e traduzir o texto resultante para outro idioma usando as APIs do Google Cloud.

## Funcionalidades

- Transcrição de voz para texto usando a API Cloud Speech-to-Text do Google Cloud.
- Tradução de texto para outro idioma usando a API Cloud Translation do Google Cloud.

## Requisitos

- Conta no Google Cloud Platform.
- Projeto do Google Cloud com os serviços Cloud Speech-to-Text e Cloud Translation ativados.
- Arquivo de áudio no formato suportado pela API de transcrição de fala do Google Cloud (como LINEAR16 para arquivos de áudio PCM).
- Credenciais de conta de serviço do Google Cloud configuradas e disponíveis como um arquivo JSON.

## Configuração

1. Clone este repositório:

git clone https://github.com/danfemarins/translate.git

2. Instale as dependências necessárias:

pip install -r requirements.txt

3. Configure as variáveis de ambiente:

export GOOGLE_APPLICATION_CREDENTIALS=/caminho/para/suas_credenciais.json

4. Execute o script:

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Notas

- Certifique-se de proteger seu arquivo de credenciais (`suas_credenciais.json`) e não compartilhá-lo publicamente.
- Este projeto é apenas um exemplo básico e pode ser expandido com mais funcionalidades, como reprodução da tradução em voz.

##                                               README FRONTEND.PY                                                         !!

 Aplicativo Desktop para Conversão de Voz para Texto e Tradução

Este é um simples aplicativo desktop que permite aos usuários selecionar um arquivo de áudio, transcrever a fala contida nele para texto e, em seguida, traduzir esse texto para outro idioma usando as APIs do Google Cloud.

## Funcionalidades

- Transcrição de voz para texto usando a API Cloud Speech-to-Text do Google Cloud.
- Tradução de texto para outro idioma usando a API Cloud Translation do Google Cloud.

## Requisitos

- Python 3.x instalado no sistema.
- Conta no Google Cloud Platform com as APIs Cloud Speech-to-Text e Cloud Translation ativadas.
- Arquivo de áudio no formato suportado pela API de transcrição de fala do Google Cloud (como LINEAR16 para arquivos de áudio PCM).
- Pacotes `google-cloud-speech` e `google-cloud-translate` instalados no ambiente Python.

## Como Usar

1. Clone este repositório:

git clone https://github.com/danfemarins/translate

2. Instale as dependências necessárias:

pip install google-cloud-speech google-cloud-translate

3. Configure as variáveis de ambiente:

export GOOGLE_APPLICATION_CREDENTIALS=/caminho/para/suas_credenciais.json

4. Execute o script `frontend.py`:

python frontend.py

5. Na interface do aplicativo, clique no botão "Selecionar Arquivo de Áudio" e escolha um arquivo de áudio.

6. Após selecionar o arquivo, o texto transcrito e traduzido será exibido na interface do aplicativo.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).