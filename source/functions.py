def get_top_level_comments(youtube, video_id):

    request = youtube.commentThreads().list(
        part='snippet',
        moderationStatus="published",
        order="time",
        textFormat="plainText",
        videoId=video_id
    )
    
    response = request.execute()
    comments = response.get('items')
    formated_comments = [
        {
            'id': comment['id'],
            'author_name': comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
            'url': comment['snippet']['topLevelComment']['snippet']['authorChannelUrl'],
            'comment': comment['snippet']['topLevelComment']['snippet']['textOriginal'],
            'date': comment['snippet']['topLevelComment']['snippet']['publishedAt'],
            'like_count': comment['snippet']['topLevelComment']['snippet']['likeCount']
        }
        for comment in comments
    ]
        
    return formated_comments



def get_child_comments_by_parent_id(youtube, parent_id):
    request = youtube.comments().list(
            part='snippet',
            textFormat="plainText",
            parentId=parent_id
         )
    response = request.execute()
    comments = response.get('items')
    
    formated_comments = [
        {
            'id': comment['id'],
            'author_name': comment['snippet']['authorDisplayName'],
            'url': comment['snippet']['authorChannelUrl'],
            'comment': comment['snippet']['textOriginal'],
            'date': comment['snippet']['publishedAt'],
            'like_count': comment['snippet']['likeCount']
        }
        for comment in comments
    ]
        
    return formated_comments