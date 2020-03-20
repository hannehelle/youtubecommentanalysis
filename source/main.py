import os
import googleapiclient.discovery
from pprint import pprint
import json, csv
from functions import get_top_level_comments, get_child_comments_by_parent_id
from settings import DEVELOPER_KEY

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    
    all_comments = []

    top_level_comments = get_top_level_comments(youtube, 'NnZ6wIwd9Ww')
    
    all_comments += top_level_comments

    for comment in top_level_comments:
        child_comments = get_child_comments_by_parent_id (youtube, comment['id'])
        all_comments += child_comments
       
    # pprint(all_comments)

    with open('comments.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['id', 'author_name', 'url', 'comment', 'date', 'like_count']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for comment_line in all_comments:
            writer.writerow(comment_line)

    
if __name__ == "__main__":
    main()