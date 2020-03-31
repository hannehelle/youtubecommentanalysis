import os
import googleapiclient.discovery
from tqdm import tqdm
from functions import get_top_level_comments, get_child_comments_by_parent_id
from settings import DEVELOPER_KEY
import re
from sentiment_analysis import text_analysis

def get_all_comments(video_id):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)


    top_level_comments = []
    current_page_comments, next_page_token = get_top_level_comments(youtube, video_id)
    top_level_comments += current_page_comments

    while next_page_token:
        current_page_comments, next_page_token = get_top_level_comments(youtube, video_id, next_page_token)
        top_level_comments += current_page_comments

    all_comments = top_level_comments.copy()

    for comment in tqdm(top_level_comments):
        child_comments = get_child_comments_by_parent_id (youtube, comment['comment_id'], comment['video_id'])
        all_comments += child_comments
    
    all_comments = text_analysis(all_comments)

    print(all_comments)
    
    return all_comments


def get_video_id(url):
    match = re.search(r"youtube\.com/.*v=([^&]*)", url)
    if match:
        return match.group(1)
    else:
        return None
