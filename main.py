from pytube import YouTube
import os
from plyer import notification
from tqdm import tqdm
from time import sleep

urlEn = input("Ingresa la url del Video de YouTube: ")

def dowload():
    yt = YouTube(urlEn)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    notification.notify(
        title='Descarga Completa :D',
        message=yt.title + ' se descargó de forma correcta.',
    )

    # Mostrar notificación de descarga completa
    print("Descarga completa")

aks = input("¿Comenzamos con la descarga? (y/n): ")

if aks.lower() == "y":
    # Descarga con barra de progreso
    for i in tqdm(range(0, 100), initial = 50, 
              desc ="Descargando espera"):
        sleep(.1)
    dowload()
else:
    print("Descarga cancelada")
