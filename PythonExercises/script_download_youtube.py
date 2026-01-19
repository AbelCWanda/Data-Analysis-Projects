#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path 


url = "https://www.youtube.com/watch?v=_hHzhijit-JK"
destino = path("pasta_video")
destino.mkdir(exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Titulo: {yt.title}\nDuracao: {yt.length}s")

yt.streams.get_highest_resolution().download(output_path=destino)
print(f"Download concluido! Video salvo em: {destino}")


# In[1]:


get_ipython().system('pip YouTube')


# In[5]:


from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path
import re

# Perguntar a URL
url = input("👉 Insira a URL do vídeo do YouTube: ")

# Diretório de destino (Downloads)
destino = Path.home() / "Downloads"
destino.mkdir(exist_ok=True)

try:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Título: {yt.title}\nDuração: {yt.length}s")

    # Sanitizar nome do ficheiro
    titulo_seguro = re.sub(r'[\\/*?:"<>|]', "_", yt.title)

    # Escolher stream com vídeo+áudio (progressivo)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

    if not stream:
        raise Exception("Nenhum stream progressivo encontrado!")

    # Fazer download
    stream.download(output_path=destino, filename=f"{titulo_seguro}.mp4")
    print(f"✅ Download concluído! Vídeo salvo em: {destino / (titulo_seguro + '.mp4')}")

except Exception as e:
    print(f"❌ Erro ao baixar vídeo: {e}")

input("Pressione ENTER para sair...")


# In[ ]:





# In[10]:


get_ipython().system('jupyter nbconvert --to script script_download_youtube.ipynb')


# In[11]:


get_ipython().system('pyinstaller --onefile script_download_youtube.py')

