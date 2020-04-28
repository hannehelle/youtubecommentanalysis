from youtube_transcript_api import YouTubeTranscriptApi

import csv
import re

import collections
import pandas as pd

from openpyxl import Workbook

video_id = 'LevQ7JZmb-0'

def get_subtitles(video_id):

    transcript_list = []
    
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru', 'en'])
    
    for sub in transcript:
        transcript_list.append(sub['text'])
        
    return transcript_list