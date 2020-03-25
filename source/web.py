from flask import Flask, request, render_template
from parsing import get_video_id, put_all_comments_in_db
from db_settings import session
from models import Comment

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        video_link = request.form.get('video_link')
        if not video_link:
            return render_template('form.html', error_message='Введите ссылку на видео')

        video_id = get_video_id(video_link)
        if not video_id:
            return render_template('form.html', error_message='Не удалось определить id видео')

        put_all_comments_in_db(video_id)

        comments = session.query(Comment).all()
        return render_template('results.html', comments=comments)





if __name__ == '__main__':
    app.run()
