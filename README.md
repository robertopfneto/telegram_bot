# Exemplos botTelegram

Descrição: Exemplos de códigos em python que funcionam como chatbots para o telegram.

Autor: Hemerson Pistori (pistori@ucdb.br)

Atualizado por Roberto Pereira de Freitas Neto (neto2014roberto@gmail.com) em 04/02/2025

### Informações sobre como foi testado

O software foi testado usando as seguintes versões de
Sistema Operacional, Linguagem e Biblioteca do Telegram

- Sistema Operacional: Ubuntu 20.04 / Windows 11
- Versão do python: 3.10.4
- Versão do telegram: 13.13
- Versão do tensorflow: 2.12.0

- 
### Gerando o chatbot no Telegram

- Instale o app do Telegram no seu celular e crie uma conta para você
- Entre no app do telegram e procure pelo usuário @botfather
- Mande a mensagem /newbot para o @botfather e vá
respondendo às perguntas que ele fizer. 
- Anote o TOKEN que ele vai gerar para você e o use no local indicado a seguir 

### Instalando as dependências no Linux (bibliotecas)

- Abra o terminal do Linux usando CTRL+ALT+T
- Verifique os ambientes conda já instalados usando o comando
abaixo. Se já tiver o ambiente chamado chatbot, não precisa executar os comandos de instalação)
```
conda env list
```

- Se já existir o ambiente conda, use o comando abaixo
para ativá-lo
```
conda activate chatbot
```

- Se o ambiente conda chatbot não existir, execute os comandos de instalação abaixo para criar o ambiente e instalar as dependências

```
conda create -y --name chatbot python=3.10
conda activate chatbot
pip install python-telegram-bot==13.13 pillow
```

- Se não tiver conda na máquina, instale usando as instruções disponíveis aqui: https://docs.conda.io/projects/miniconda/en/latest/ (Use o Quick Command Line install para Linux)

- Para rodar o modelo criado através do TeachableMachine, será necessária instalar também as seguintes dependências:

```
pip install tensorflow==2.12.0

```


### Iniciando o seu chatbot

- Use o botão ao lado de 'Clone' ou o botão 'Code' (role para a parte de cima desta tela) para baixar para a sua máquina o arquivo compactado (.zip) contendo estes códigos em python
- Entre na pasta Downloads usando o comando abaixo
```
cd Downloads
```
- Use o comando abaixo para ver todos os arquivos que terminam com zip que estão na pasta Downloads para conferir
se baixou direito
```
ls *zip
```
- Descompacte o arquivo usando o comando abaixo
```
unzip 'bot_tel*'
```
- Entre na pasta descompactada
```
cd bot_telegram-master
```

- Rode o comando abaixo para iniciar o seu BOT. Não esqueça de trocar pelo TOKEN que você criou anteriormente usando o @botfather

```
python botTelegram.py SEU_TOKEN_AQUI 
```

- Teste o código mandando um "Oi" no chat do bot, se funcionou, aperte CNTRL + C para finalizar a execução do bot

### Implementando o nosso modelo de rede neural no código

- Acesse o link abaixo e logue em sua conta:

`https://teachablemachine.withgoogle.com/train/image`

- Selecione "Image Project" e "Standart Tool"
- Crie as classes que desejar e insira as imagens, após isto basta treinar o modelo com as configurações padrão
- Selecione o botão "Export Model" e vá até a aba "TensorFlow" e faça o download do modelo

- Vá no gerenciador de arquivos e extraia o arquivo .zip baixado
- Mova o arquivo descompactado até a pasta `modelo` dentro a pasta onde o código está localizado

# Testando implementação

- Execute novamente o comando, seguindo as instruções que o bot mandar

 ```
python botTelegram.py SEU_TOKEN_AQUI 
```

Exemplo: 

![image](https://github.com/user-attachments/assets/ad01587b-ed2a-42c7-8454-3685bf592aa6)

