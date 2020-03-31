from datetime import datetime
from settings import DEVELOPER_KEY

def get_top_level_comments(youtube, video_id, page_token=None):

    request = youtube.commentThreads().list(
        part='snippet',
        moderationStatus="published",
        order="time",
        videoId=video_id,
        maxResults=2,
        pageToken=page_token,
        textFormat="plainText"
    )

    
    response = request.execute()

    next_page_token = response.get('nextPageToken')

    comments = response.get('items')
    formated_comments = [
        {
            'video_id': comment['snippet']['videoId'],
            'comment_id': comment['id'],
            'author_name': comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
            'url': comment['snippet']['topLevelComment']['snippet']['authorChannelUrl'],
            'comment': comment['snippet']['topLevelComment']['snippet']['textOriginal'],
            'date': datetime.strptime(comment['snippet']['topLevelComment']['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%S.%fZ"),
            'like_count': comment['snippet']['topLevelComment']['snippet']['likeCount']
        }
        for comment in comments
    ]
        
    return formated_comments, next_page_token



def get_child_comments_by_parent_id(youtube, parent_id, video_id):
    request = youtube.comments().list(
            part='snippet',
            textFormat="plainText",
            parentId=parent_id
         )
    response = request.execute()
    comments = response.get('items')
    
    formated_comments = [
        {
            'video_id': video_id,
            'comment_id': comment['id'],
            'author_name': comment['snippet']['authorDisplayName'],
            'url': comment['snippet']['authorChannelUrl'],
            'comment': comment['snippet']['textOriginal'],
            'date': datetime.strptime(comment['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%S.%fZ"),
            'like_count': comment['snippet']['likeCount']
        }
        for comment in comments
    ]
        
    return formated_comments

print(__name__)