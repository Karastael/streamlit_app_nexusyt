import yt_dlp
#IGNORAR!
#Archivo de pruebas



select_format = input("Escribí la opción a descargar (MP3 O VIDEO)").lower()
url = input("Pega la URL del video: ")

#OPCIÓN PARA MP3
if select_format == "mp3":
    opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
          }],
}

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])


#OPCIÓN PARA MP4
if select_format == "mp4":

    ydl_opts = {}  # Opciones (por ahora vacío)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
#EN EL CASO DE NO SER MP4 O MP3
elif select_format != "mp4" or select_format == "mp3":
    print("Debes seleccionar un tipo de formato!")