from flask import Flask, request, render_template
<<<<<<< HEAD
from parsing import get_video_id, get_all_comments
=======
from parsing import get_video_id, put_all_comments_in_db
>>>>>>> da559716c726734437be911cb5fdb0219b7519ba
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

<<<<<<< HEAD
        comments = get_all_comments(video_id)
        
        return render_template('results.html', comments=comments)

=======
        put_all_comments_in_db(video_id)

        comments = session.query(Comment).all()
        return render_template('results.html', comments=comments)





>>>>>>> da559716c726734437be911cb5fdb0219b7519ba
if __name__ == '__main__':
    app.run()
