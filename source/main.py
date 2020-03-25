import os
import httplib2
import json, csv
import googleapiclient.discovery

from tqdm import tqdm

from pprint import pprint
from apiclient.discovery import build_from_document
from apiclient.errors import HttpError

from functions import get_top_level_comments, get_child_comments_by_parent_id
from settings import DEVELOPER_KEY
from db_settings import Base, session
from models import Comment

VIDEO_ID = 'jgYrnFqkHKI'

def get_all_comments(video_id):


    Base.metadata.create_all()

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    
    top_level_comments = []
    current_page_comments, next_page_token = get_top_level_comments(youtube, video_id)
    top_level_comments += current_page_comments

    while next_page_token:
        current_page_comments, next_page_token = get_top_level_comments(youtube, video_id, next_page_token)
        top_level_comments += current_page_comments

    print(len(top_level_comments))

    all_comments = top_level_comments.copy()

    for comment in tqdm(top_level_comments):
        child_comments = get_child_comments_by_parent_id (youtube, comment['comment_id'], comment['video_id'])
        all_comments += child_comments
    
    print(len(all_comments))
    
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

    # authors = [author[0] for author in session.query(Comment.author_name).distinct().all()]

    # comment_counts = {}

    # for author in authors:
    #     value = session.query(Comment).filter(Comment.author_name == author).count()
    #     comment_counts[author] = value
    # print(comment_counts)


get_all_comments(VIDEO_ID)