"""
Created on Mon Aug 9 16:32:32 2021
@author: amali
"""

import argparse


import pafy
import numpy as np
from IPython.display import Audio
from scipy.io import wavfile
from pydub import AudioSegment
import os
import glob
from bs4 import BeautifulSoup,NavigableString, Tag
import re, requests, urllib.parse, urllib.request



# =================================================================================================
def get_albums(data):

      """
      args :
        data : variable soup tag elements of results_albums
      output :
        results : list str of albums
      """

      results = []

      for i in data :
        result = ''
        for j in range(len(i.contents)) :
          if isinstance(i.contents[j], NavigableString):
            continue
          if isinstance(i.contents[j], Tag):
            result += ' '+ i.contents[j].span.contents[0]
        results.append(result)

      return results
      
# =================================================================================================
def get_titles(data) :
      """
      args :
        data : variable soup tag elements of results_titles
      output :
        titles : list str of titles
      """
      titles = []

      for i in results_titles:
          titles.append(i.contents[0])

      return titles
      
# =================================================================================================
    
def search_music(music_name) :
    """
    args :
      music_name : str music name to search in youtube
    outputs :
    Tuple
      1 : title of music
      2 : youtube url
    """
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    
    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for music in yt_title:
        pass

    return music["content"], "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    
    
# =================================================================================================
def download_music(data):

      """
      args :
          tuple
          1 : title of music
          2 : youtube url
      outputs :
          download music and convert it to mp3 format
      """
      if not os.path.exists("./dataset1"):
        os.makedirs("./dataset1")
      if not os.path.exists("./dataset"):
        os.makedirs("./dataset")

      for search in data :

        url = search[1]
        video = pafy.new(url)
        best = video.getbest()
        audio = video.getbestaudio()
        audio.download("./dataset1")

      for f in glob.glob("./dataset1/*") :
        
        title_name = f.split('/')[-1].split('.')[0]
        title_format = f.split('/')[-1].split('.')[1]
        wav_audio = AudioSegment.from_file(f, format=title_format)
        wav_audio.export("./dataset/"+title_name+'.mp3', format="mp3")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('url', '--url', help='insert url of a spotify list (default chessbrah playlist)', type=str,default="https://open.spotify.com/playlist/3Oc7Q4BbPLYxVyzoTblu8O")
    
    args = parser.parse_args()
    
    # =================================================================================================
    # Webscraping the spotify playlist
    # parse the html using beautiful soup and store in variable 'soup'
    
    page = urllib.request.urlopen(args.url)
    soup = BeautifulSoup(page, 'html.parser')
    
    # =================================================================================================
    # extracting all divs with the name 'span' and with the specific class
    
    results_titles = soup.find_all('span',class_='track-name')
    results_albums = soup.find_all('span',class_='artists-albums')
      
    # =================================================================================================
    # search_queries : key words ( track title + album title ) to look for in youtube's search engine
    
    search_queries = [get_titles(results_titles)[i] + ' '+ get_albums(results_albums)[i] for i in range(len(get_albums(results_albums)))]
    
    # =================================================================================================
    # List of all urls of the playlist
    url_music = [search_music(music_name) for music_name in search_queries]
       
    # =================================================================================================    
    download_music(url_music)