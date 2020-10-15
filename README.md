# Backing-track-creator
A Python script for removing center channel lead instruments from stereo audio files

# Dependencies 
pip install pydub

pip install youtube_dl

# Quick Start 
~ python btc.py

[paste youtube link]

backing track file will be downloaded to parent directory 

or use the api:
```
https://www.SheltonTolbert.com/api/btc?url='youtube-link'
```
** Please do not download any content that you do not already own **

# How does it work? 

The backing track creator # Backing-track-creator
A Python script for removing center channel lead instruments from stereo audio files


# Okay, but how does really it work? 

The backing track creator utilises the pydub library to extract the left and right channels from a stereo track. By inverting the phase of the left channel and recombining the left and right channels, we are left with a track where the center channel is removed. 
We can express this process in the following expression: 

stereo.mp3 = left + right

left = left + center
right = right + center 
-left = -left + -center 

-left + right = (-left + -center) + (center + right)
 
#the two center channels cancel out (center - center) and we are left with (-left + right)



