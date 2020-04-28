from utilits import get_video_id
from parsing import get_all_comments
from get_subs import get_subtitles
from counter import words_counter


def all_data(video_id):
    comments_list = []
    data = []
    
    all_comments = get_all_comments(video_id)

    for comment in all_comments:
        comments_list.append(comment['comment'])

    print ('Получил коммент в комментс: ')

    comment_words_counter = words_counter(comments_list)

    print("Посчитал слова в комментариях")
    
    subtitles = get_subtitles(video_id)

    print ('Получил субтитры')

    subtitles_counter = words_counter(subtitles)

    print ('Посчитал субтитры')

    data.append(all_comments)
    data.append(comment_words_counter)
    data.append(subtitles_counter)
    
    return data