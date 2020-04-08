from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import csv

def text_analysis (all_comments):
    texts = [comment['comment'] for comment in all_comments]

    tokenizer = RegexTokenizer()

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(texts, k=5)
    
    for i, sentiment in enumerate(results):
        all_comments[i]['positive'] = sentiment['positive']
        all_comments[i]['negative'] = sentiment['negative']
        all_comments[i]['neutral'] = sentiment['neutral']
    
    with open('analysis.csv', 'w', encoding='utf-8') as f:
        fields = ['author_name', 'comment', 'date', 'url', 'comment_id', 'video_id', 'like_count', 'positive', 'negative', 'neutral']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for i in all_comments:
            writer.writerow(i)

    return all_comments