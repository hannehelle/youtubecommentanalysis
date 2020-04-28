from flask import Flask, request, render_template
from flask import send_file
from models import Comment
from utilits import get_video_id
from create_data import all_data
from write_xls import write_xls

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

        data = all_data(video_id)
        write_xls(video_id, data)

        return render_template('downloads.html')

@app.route('/file-downloads/', methods = ['POST'])
def file_downloads():
	try:
		return render_template('downloads.html')
	except Exception as e:
		return str(e)

@app.route('/return-files/', methods = ['GET'])
def return_files_tut():
	try:
		return send_file('{}.xlsx'.format(video_id), attachment_filename='{}.xlsx'.format(video_id), as_attachment=True)
	except Exception as e:
		return str(e)


if __name__ == '__main__':
    app.run()
