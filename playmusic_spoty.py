'''
    Description:
    Play music on Spotify with python.

    Author: AlejandroV
    Version: 1.0
    Video: https://youtu.be/Vj64pkXtz28
'''
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web
import pyautogui
from time import sleep

# your credentials
client_id = 'YOUR_CLIENT_ID_HERE'
client_secret = 'YOUR_CLIENT_SECRET_HERE'
flag = 0

# artist and name of the song
author = ''
song = 'bad guy'.upper()

if len(author) > 0:
    # authenticate
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    result = sp.search(author)

    for i in range(0, len(result["tracks"]["items"])):
        # songs by artist
        name_song = result["tracks"]["items"][i]["name"].upper()

        if song in name_song:
            flag = 1
            web.open(result["tracks"]["items"][i]["uri"])
            sleep(5)
            pyautogui.press("enter")
            break

# if song by artist not found
if flag == 0:
    song = song.replace(" ", "%20")
    web.open(f'spotify:search:{song}')
    sleep(5)
    for i in range(18):
        pyautogui.press("tab")

    for i in range(2):
        pyautogui.press("enter")
        sleep(1)