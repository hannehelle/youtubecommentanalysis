import os
import googleapiclient.discovery
from tqdm import tqdm
from functions import get_top_level_comments, get_child_comments_by_parent_id
from settings import DEVELOPER_KEY

from sentiment_analysis import text_analysis
import time
from settings import api_service_name, api_version
from models import Comment


def get_all_comments(video_id):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

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
    
    all_comments = text_analysis(all_comments)

    end = time.time()

    print('Время выполнения функции: ', end - start)
    
    return all_comments