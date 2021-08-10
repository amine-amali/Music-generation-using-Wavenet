# Music-generation-using-Wavenet
## Requierements
!pip install pydub
!pip install pafy
!pip install youtube_dl
!pip install vlc
!pip install tensorflow==1.15
!pip install librosa==0.5
## Description
1. Webscraping the spotify playlist of [chessbrah](https://open.spotify.com/playlist/3Oc7Q4BbPLYxVyzoTblu8O), and downloading the corresponding playlist at youtube to mp3 format.

2. Implementation of [WaveNet](https://github.com/ibab/tensorflow-wavenet/) to generate techno music.

Trained on 100 steps and the model generates noisy sound. Looking at the instructions, the model need to be trained on at least 80K steps.

Considering on average the model takes 30 seconds/step (with free Google colab resources), this will lead us to 1 month for training !!!
