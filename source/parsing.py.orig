import os
import googleapiclient.discovery
from tqdm import tqdm
from functions import get_top_level_comments, get_child_comments_by_parent_id
from settings import DEVELOPER_KEY
from db_settings import session
import re
from sentiment_analysis import text_analysis
import time
from settings import api_service_name, api_version
from models import Comment
<<<<<<< HEAD:source/parsing.py


def get_all_comments(video_id):
=======
import re


def put_all_comments_in_db(video_id):
    Base.metadata.create_all()

>>>>>>> da559716c726734437be911cb5fdb0219b7519ba:source/parsing.py
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
<<<<<<< HEAD:source/parsing.py

=======
>>>>>>> da559716c726734437be911cb5fdb0219b7519ba:source/parsing.py

    top_level_comments = []
    current_page_comments, next_page_token = get_top_level_comments(youtube, video_id)
    top_level_comments += current_page_comments

    start = time.time()

    while next_page_token:
        current_page_comments, next_page_token = get_top_level_comments(youtube, video_id, next_page_token)
        top_level_comments += current_page_comments

    all_comments = top_level_comments.copy()

    for comment in tqdm(top_level_comments):
        child_comments = get_child_comments_by_parent_id (youtube, comment['comment_id'], comment['video_id'])
        all_comments += child_comments
    
<<<<<<< HEAD:source/parsing.py
    all_comments = text_analysis(all_comments)

    end = time.time()

    print('Время выполнения функции: ', end - start)
    
    return all_comments


def get_video_id(url):
    match = re.search(r"youtube\.com/.*v=([^&]*)", url)
    if match:
        return match.group(1)
    else:
        return None

def add_to_db (all_comments):
=======
>>>>>>> da559716c726734437be911cb5fdb0219b7519ba:source/parsing.py
    session.query(Comment).delete()
    session.commit()

    for comment in all_comments:
        c = Comment(
            video_id=comment['video_id'],
            comment_id=comment['comment_id'],
            author_name=comment['author_name'],
            url=comment['url'],
            comment=comment['comment'], 
            date=comment['date'],
            like_count=comment['like_count']
        )
        session.add(c)
    session.commit()

<<<<<<< HEAD:source/parsing.py
add_to_db(all_comments)
=======

def get_video_id(url):
    match = re.search(r"youtube\.com/.*v=([^&]*)", url)
    if match:
        return match.group(1)
    else:
        return None
>>>>>>> da559716c726734437be911cb5fdb0219b7519ba:source/parsing.py
