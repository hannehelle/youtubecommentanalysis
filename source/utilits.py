import re
from db_settings import session

def get_video_id(url):
    match = re.search(r"youtube\.com/.*v=([^&]*)", url)
    if match:
        return match.group(1)
    else:
        return None

def add_to_db (all_comments):
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
    session.commit()
    session.add(c)