from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import csv
import re

import pandas as pd

def text_analysis (all_comments):

    texts = [comment['comment'] for comment in all_comments]

    tokenizer = RegexTokenizer()

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(texts, k=5)
    
    for i, sentiment in enumerate(results):
        all_comments[i]['positive'] = sentiment['positive']
        all_comments[i]['negative'] = sentiment['negative']
        all_comments[i]['neutral'] = sentiment['neutral']

    return all_comments