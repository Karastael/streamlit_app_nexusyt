import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Nexus YT - By JuanDV", page_icon="📽️")
st.subheader("Nexus YT Downloader V 1.0 🛰️")

url = st.text_input("Pega la URL:")

if url:
    formato = st.radio("Elige el formato:", ("MP3 🎧", "MP4 🎞️"))

    if st.button("Descargar"):
        if formato == "MP3 🎧":
            opts = {
                "format": "bestaudio/best",
                "outtmpl": "temp_audio.%(ext)s",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }
        else:
            opts = {
                "format": "best",
                "outtmpl": "temp_video.%(ext)s"
            }

        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url)
            filename = ydl.prepare_filename(info)
            if formato == "MP3 🎧":
                filename = filename.rsplit('.', 1)[0] + ".mp3"

        st.success(f"¡Descarga completada: {os.path.basename(filename)}!")

        # Botón para que el usuario guarde el archivo en su PC
        with open(filename, "rb") as f:
            st.download_button("Guardar en tu PC", f, file_name=os.path.basename(filename))

        os.remove(filename)
else:
    st.warning("Por favor ingresa una URL antes de descargar.")
