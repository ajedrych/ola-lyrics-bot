![ola lyrics bot](Images/image.png)
# ola lyrics bot

Connect to [Spotify](https://open.spotify.com/playlist/2VQxlEsq39DGjFxJ0o5nMo?si=6c5ad4f44d9544be) and Genius to post lyrics on [Twitter](https://twitter.com/olalyricsbot)

#### 🔧 Install

To run it locally, you will need to install libraries:

    import spotipy
    import spotipy.oauth2 as oauth2
    from spotipy.oauth2 import SpotifyOAuth
    from spotipy.oauth2 import SpotifyClientCredentials
    import lyricsgenius    
    import tweepy    
    import random   
    import os   
    from dotenv import load_dotenv

#### What else can be added?

 - [ ] bot deployment
 - [ ] function, which checks the length of last_seen_ids.txt and keeps only the 10 most recent tweet id

#### 🎓 Project

Ola lyrics bot was made as a course credit project.

*Faculty of Economic Sciences, University of Warsaw,
Wprowadzenie do programowania w języku Python, January 2022* 