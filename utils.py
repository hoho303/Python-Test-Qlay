from pytube import YouTube
from pydub import AudioSegment
import os
import json
import re

def clean_text(text):
    text = text.lower()
    text = re.sub('[^A-Za-z0-9 ]+', '', text)
    return text

def get_diff(s1, s2):
    s1 = clean_text(s1)
    s2 = clean_text(s2)
    
    # get words difference between two strings
    s1 = set(s1.split())
    s2 = set(s2.split())

    t_diffs = list(s1.difference(s2))

    return t_diffs

def download_audio_youtube(url, output_path='temp_audio'):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    dest = "temp_audio"
    out_file = video.download(output_path=dest)
    base, ext = os.path.splitext(out_file)

    audio = AudioSegment.from_file(out_file)
    base = base.replace(' ', '_')
    new_file = base + '.wav'
    audio.export(new_file, format='wav')

    os.remove(out_file)
    print(new_file)

    return new_file

def export_file(res, out_file):
    with open(out_file, 'w') as f:
        json.dump({'data': res}, f)