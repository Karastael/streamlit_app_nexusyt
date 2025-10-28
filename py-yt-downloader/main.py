import streamlit as st, yt_dlp

#Ícono de la ventana
st.set_page_config(page_title="Nexus YT - By JuanDV", page_icon="📽️")

#Header representativo
st.subheader("Nexus YT Downloader V 1.0 🛰️")

#Ingreso de la URL
url = st.text_input("Pega la URL: ")



#FORMATOS
#-------------- MP3 ----------------
if st.checkbox(label="MP3 🎧"):

    opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
          }],
}
    if st.button(label="Descargar MP3"):
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])


#-------------- MP4 -----------------
if st.checkbox(label="MP4 O VIDEO 🎞️"):

    opts = {} #Por defecto, video en HQ disponible
    if st.button(label="Descargar MP4 O VIDEO"):
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])

