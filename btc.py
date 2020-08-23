from __future__ import unicode_literals
import pydub
import youtube_dl
from pydub import AudioSegment
from pydub.playback import play
import os

def get_file_name():
    for files in os.listdir():
        if 'mp3' in str(files):
            return(str(files))
    return None

def flip_phase(mp3):
    inverted = AudioSegment.from_file(mp3, format="mp3").invert_phase()
    inverted.export("invertedL.mp3", format="mp3")

def download(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def split_track(file):
    stereo_track = AudioSegment.from_file(file)
    return(stereo_track.split_to_mono())

def export(tracks):
    tracks[0].export("exportL.mp3", format="mp3")
    tracks[1].export("exportR.mp3", format="mp3")

def combine(track1, track2):
    track1 = AudioSegment.from_file(track1, format="mp3")
    track2 = AudioSegment.from_file(track2, format="mp3")
    track1.overlay(track2).export("backing-track.mp3", format="mp3")

def clean_up():
    names = ['exportL.mp3', 'exportR.mp3', 'invertedL.mp3']
    for files in os.listdir():
        if files in names:
            os.remove(files)

if __name__ == "__main__":
    print("Insert the link")
    download(input (""))
    file = get_file_name()
    tracks = split_track(file)
    export(tracks)
    flip_phase('exportL.mp3')
    combine('exportR.mp3', 'invertedL.mp3')
    clean_up()