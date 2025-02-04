import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys

# Lê o token do Telegram como argumento na linha de comando
MEU_TOKEN = sys.argv[1]

# Pasta para salvar imagens enviadas
pasta_imgs = './Telegram_Imagens_Recebidas/'
os.makedirs(pasta_imgs, exist_ok=True)

# Carrega o modelo Keras e as classes
modelo_path = "./modelo/keras_model.h5"
labels_path = "./modelo/labels.txt"
model = tf.keras.models.load_model(modelo_path, compile=False)
class_names = open(labels_path, "r").readlines()

print('Carregando BOT usando o token', MEU_TOKEN)

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para responder mensagens de texto
def echo(update, context):
    texto = update.message.text.lower()

    if texto in map(str.lower, ['Olá', 'Oi', 'Bom dia', 'Boa Tarde', 'Boa noite', 'Como vai?']):
        update.message.reply_text('Olá, tudo bem?')
    
    elif texto in map(str.lower, ['Tudo sim', 'Tudo bem', 'Estou bem']):
        update.message.reply_text('Que bom! Deseja enviar uma imagem para eu avaliar?')
    
    elif texto in map(str.lower, ['Não', 'Não quero', 'Não desejo']):
        update.message.reply_text('Ok, se precisar de algo estarei por aqui!')

    elif texto in map(str.lower, ['Sim', 'Quero', 'Desejo']):
        update.message.reply_text('Ok, envie a imagem que deseja que eu avalie!')    
    

# Dicionário com descrições das classes
descricoes_classes = {
    "Onça": "🐆 A onça-pintada é o maior felino das Américas e um símbolo do Pantanal. Excelente nadadora e caçadora furtiva!",
    "Anta": "🦣 A anta é o maior mamífero terrestre do Brasil! Ela ajuda a espalhar sementes, sendo essencial para o ecossistema.",
    "Capivara": "🦫 A capivara é o maior roedor do mundo! Vive em grupos próximos à água e é conhecida por sua natureza pacífica."
}

def processa_imagem(update, context):
    # Pega o identificador da última imagem enviada
    identificador = update.message.photo[-1].file_id
    arquivo = context.bot.get_file(identificador)

    # Baixa o arquivo
    nome_imagem = os.path.join(pasta_imgs, f"{identificador}.jpg")
    arquivo.download(nome_imagem)
    print(f'Processando arquivo {nome_imagem}')

    # Abre a imagem e prepara para a IA
    image = Image.open(nome_imagem).convert("RGB")

    # Redimensiona para 224x224
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Converte para array numpy
    image_array = np.asarray(image)

    # Normaliza a imagem
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Prepara o array para o modelo
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Faz a predição
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip().split(" ", 1)[-1]  # Corrige para pegar apenas o nome da classe
    confidence_score = prediction[0][index]

    # Pega a descrição correspondente
    descricao = descricoes_classes.get(class_name, "Não tenho informações sobre este animal.")

    # Envia resposta ao usuário
    resposta = f"📸 *Identifiquei:* {class_name}\n📊 *Confiança:* {confidence_score:.2%}\n\n{descricao}"
    update.message.reply_text(resposta, parse_mode="Markdown")


# Respostas para comandos
def start(update, context):
    update.message.reply_text('Olá, já comecei! Envie uma mensagem ou uma imagem para eu identificar.')

def help(update, context):
    update.message.reply_text('Eu posso identificar imagens. Envie uma e eu tento reconhecer!')

# Captura erros
def error(update, context):
    logger.warning('Erro "%s" na operação "%s"', context.error, update)

# Função principal
def main():
    updater = Updater(MEU_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Adiciona handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, processa_imagem))
    dp.add_error_handler(error)

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print('Bot respondendo, use CTRL+C para parar')
    main()
