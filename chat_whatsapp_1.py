"""Bilbiotecas que serão utilizadas"""
import pywhatkit
import keyboard
import time
from datetime import datetime

"""**** Vaiáveis ****"""
contatos = ['+55839xxxxxxxx', '+55839xxxxxxxx', '+55839xxxxxxxx'] #Lista de contatos
#O contato deve ser escrito em string,utilizando do DDI (+55 para o Brasil) e o DDD da região.

"""**** Main ****"""
for i in range(len(contatos)):
    pywhatkit.sendwhatmsg(contatos[i], "Hello World", datetime.now().hour, datetime.now().minute + 1) #Abre o whatsappWeb e digita a mensagem escolhida
    time.sleep(30) #Tempo necessário pra o site abrir e carregar a mensagem
    keyboard.press_and_release('ctrl + w') #Fecha a aba do WhatsappWeb que foi criada
