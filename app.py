from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

def descargar_video(url, ruta_descarga='.'):
    try:
        video = YouTube(url)
        video.streams.get_highest_resolution().download(output_path=ruta_descarga)
        return True, "Video descargado correctamente."
    except Exception as e:
        return False, f"Error al descargar el video: {e}"

def descargar_audio(url, ruta_descarga='.'):
    try:
        video = YouTube(url)
        audio_stream = video.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=ruta_descarga)
        return True, "Audio descargado correctamente."
    except Exception as e:
        return False, f"Error al descargar el audio: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ''
    if request.method == 'POST':
        url = request.form['url']
        opcion = request.form['opcion']

        if opcion == 'video':
            success, mensaje = descargar_video(url)
        elif opcion == 'audio':
            success, mensaje = descargar_audio(url)

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

#from flask import Flask, render_template, request
#from pytube import YouTube
#import os
#app = Flask(__name__)
#def descargar_video(url, carpeta_destino='.', nombre_archivo=None):
#    try:
#        video = YouTube(url)
#        if nombre_archivo is None:
#            nombre_archivo = video.title
#        carpeta_destino = os.path.join(carpeta_destino, 'videos')
#        os.makedirs(carpeta_destino, exist_ok=True)
#        video.streams.get_highest_resolution().download(output_path=carpeta_destino, filename=nombre_archivo)
 #       return True, f"Video descargado correctamente en '{carpeta_destino}'."
  #  except Exception as e:
   #     return False, f"Error al descargar el video: {e}"

#def descargar_audio(url, carpeta_destino='.', nombre_archivo=None):
#    try:
 #       video = YouTube(url)
  #      if nombre_archivo is None:
   #         nombre_archivo = video.title
    #    carpeta_destino = os.path.join(carpeta_destino, 'audios')
     #   os.makedirs(carpeta_destino, exist_ok=True)
      #  audio_stream = video.streams.filter(only_audio=True).first()
       # audio_stream.download(output_path=carpeta_destino, filename=nombre_archivo)
        #return True, f"Audio descargado correctamente en '{carpeta_destino}'."
    #except Exception as e:
     #   return False, f"Error al descargar el audio: {e}"

#@app.route('/', methods=['GET', 'POST'])
#def index():
 #   mensaje = ''
  #  if request.method == 'POST':
   #     url = request.form['url']
    #    opcion = request.form['opcion']

     #   if opcion == 'video':
      #      carpeta_destino = 'videos'  
       #     success, mensaje = descargar_video(url, carpeta_destino)
       # elif opcion == 'audio':
        #    carpeta_destino = 'audios'  
         #   success, mensaje = descargar_audio(url, carpeta_destino)

   # return render_template('index.html', mensaje=mensaje)

#if __name__ == '__main__':
 #   app.run(debug=True)
