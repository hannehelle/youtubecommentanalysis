from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

def text_analysis (all_comments):
    texts = [comment['comment'] for comment in all_comments]

    tokenizer = RegexTokenizer()

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(texts, k=3)
    
    for i, sentiment in enumerate(results):
        all_comments[i]['sentiment'] = sentiment
    
    return all_comments