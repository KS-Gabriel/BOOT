import data as data
import telebot
from datetime import datetime, date

CHAVE_API = "5135694115:AAGApN1vWgbyjGwZStFV73i_AC8zpBG_FHs"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["abraco"])
def abraco(mensagem):
    bot.send_message(mensagem.chat.id, "Um Forte Abraço Camarada!!")


@bot.message_handler(commands=["dia"])
def dia(mensagem):
    num = date.today().weekday()

    sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

    if num < 5:
        dia_da_semana = (f"Tenha uma boa {sem[num]}-feira =D")
    else:
        dia_da_semana = (f"Tenha um bom {sem[num]} =D")

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

    bot.send_message(mensagem.chat.id, data_e_hora_em_texto + " - " + dia_da_semana)


@bot.message_handler(commands=["dica"])
def dica(mensagem):
    bot.send_message(mensagem.chat.id, "Estude meu caro Camarada!!")


@bot.message_handler(commands=["imagem"])
def imagem(mensagem):
    bot.reply_to(mensagem, "Ainda Não há Nada Aqui, Lamentamos!!")


@bot.message_handler(commands=["imc"])
def imc(mensagem):

    bot.reply_to(mensagem, "imc = peso / (altura²)")


@bot.message_handler(commands=["links"])
def links(mensagem):
    texto = """
        Escolha Um Comando Abaixo:

        /amazon
        /discord
        /facebook
        /github
        /gmail
        /google
        /googleclassrom
        /googledrive
        /googletradutor
        /instagram
        /microsoft
        /outlook
        /snapchat
        /stackoverflow
        /telegram
        /twiter
        /whatsapp
        /wpsoffice
        /youtube
        """
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["amazon"])
def amazon(mensagem):
    bot.send_message(mensagem.chat.id, 'https://www.amazon.com.br')


@bot.message_handler(commands=["discord"])
def discord(mensagem):
    bot.send_message(mensagem.chat.id, 'https://discord.com')


@bot.message_handler(commands=["facebook"])
def facebook(mensagem):
    bot.send_message(mensagem.chat.id, 'https://pt-br.facebook.com')


@bot.message_handler(commands=["github"])
def github(mensagem):
    bot.send_message(mensagem.chat.id, 'https://github.com')


@bot.message_handler(commands=["gmail"])
def gmail(mensagem):
    bot.send_message(mensagem.chat.id, 'https://mail.google.com')


@bot.message_handler(commands=["google"])
def google(mensagem):
    bot.send_message(mensagem.chat.id, 'https://google.com')


@bot.message_handler(commands=["googleclassrom"])
def googleclassrom(mensagem):
    bot.send_message(mensagem.chat.id, 'https://classroom.google.com')


@bot.message_handler(commands=["googledrive"])
def googledrive(mensagem):
    bot.send_message(mensagem.chat.id, 'https://drive.google.com')


@bot.message_handler(commands=["googletradutor"])
def googletradutor(mensagem):
    bot.send_message(mensagem.chat.id, 'https://translate.google.com.br')


@bot.message_handler(commands=["instagram"])
def instagram(mensagem):
    bot.send_message(mensagem.chat.id, 'https://www.instagram.com')


@bot.message_handler(commands=["microsoft"])
def microsoft(mensagem):
    bot.send_message(mensagem.chat.id, 'https://www.microsoft.com')


@bot.message_handler(commands=["outlook"])
def outlook(mensagem):
    bot.send_message(mensagem.chat.id, 'https://outlook.live.com/')


@bot.message_handler(commands=["snapchat"])
def snapchat(mensagem):
    bot.send_message(mensagem.chat.id, 'https://www.snapchat.com')


@bot.message_handler(commands=["stackoverflow"])
def stackoverflow(mensagem):
    bot.send_message(mensagem.chat.id, 'https://stackoverflow.com')


@bot.message_handler(commands=["telegram"])
def telegram(mensagem):
    bot.send_message(mensagem.chat.id, 'https://telegram.org')


@bot.message_handler(commands=["twiter"])
def twiter(mensagem):
    bot.send_message(mensagem.chat.id, 'https://twitter.com')


@bot.message_handler(commands=["whatsapp"])
def whatsapp(mensagem):
    bot.send_message(mensagem.chat.id, 'https://www.whatsapp.com')


@bot.message_handler(commands=["wpsoffice"])
def wpsoffice(mensagem):
    bot.send_message(mensagem.chat.id, 'https://www.wps.com')


@bot.message_handler(commands=["youtube"])
def youtube(mensagem):
    bot.send_message(mensagem.chat.id, 'https://www.youtube.com')


@bot.message_handler(commands=["musica"])
def musica(mensagem):
    bot.reply_to(mensagem, "Ainda Não há Nada Aqui, Lamentamos!!")


@bot.message_handler(commands=["my"])
def my(mensagem):
    texto = """

        /boanoite - Kill BOT """

    bot.reply_to(mensagem, "Acesso Não Permitido!")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha Um Comando Abaixo:
    
    /abraco Quero Abraço
    /dia      - Que dia é Hoje?
    /dica     - O Que Fazer!
    /imagem   - (Do Que?)
    /imc      - Indice de Maça Corporal
    /links    - (Site?)
    /musica   - (Nome Da Musica)
    /my       - $MY$
    
    Responder Qualquer outra coisa não irá funcionar."""
    bot.reply_to(mensagem, texto)


bot.polling()
