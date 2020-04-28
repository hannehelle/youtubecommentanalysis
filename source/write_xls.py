import pandas as pd
import numpy as np
from openpyxl import Workbook, load_workbook
import xlsxwriter

def write_xls(video_id, data):
    
    workbook = Workbook()

    all_comments = data[0]
    comments_words_counter = data [1]
    subtitles_words_counter = data[2]

    df_all_comments = pd.DataFrame(all_comments,
        columns=['author_name', 'comment', 'date', 'url', 'comment_id', 'video_id', 'like_count', 'positive', 'negative', 'neutral'])

    df_comments_words_counter = pd.DataFrame.from_dict(data=comments_words_counter,
        orient='index', columns=['counter']).sort_values('counter', ascending=False)


    df_subtitles_words_counter = pd.DataFrame.from_dict(data=subtitles_words_counter,
        orient='index', columns=['counter']).sort_values('counter', ascending=False)


    with pd.ExcelWriter('{}.xlsx'.format(video_id)) as writer:  
        df_all_comments.to_excel(writer, sheet_name='all_comments')
        df_comments_words_counter.to_excel(writer, sheet_name='comments_words_counter')
        df_subtitles_words_counter.to_excel(writer, sheet_name='subtitles_words_counter')


    a = "Все записано в XLS"

    return a