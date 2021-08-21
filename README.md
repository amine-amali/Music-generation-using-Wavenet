# Music-generation-using-Wavenet

## Description
1. Webscraping the spotify playlist of [chessbrah](https://open.spotify.com/playlist/3Oc7Q4BbPLYxVyzoTblu8O), and downloading the corresponding playlist to mp3 format.

Webscraping => Getting the playlist => Use Youtube_dl API to download the playlist => Converting the music videos clips to mp3 format.

2. Training the model [WaveNet](https://github.com/ibab/tensorflow-wavenet/) to learn to generate techno music.

Trained on 100 steps and the model generates noisy sound. Looking at the instructions, the model need to be trained on at least 80K steps.


