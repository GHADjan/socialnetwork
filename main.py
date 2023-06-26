from flask import Flask, render_template
from comment.comment import comment_bp
from hashtag.hashtag import hashtag_bp
from photo.photo_api import photo_bp
from user.user_api import user_bp
from posts.post_api import post_bp


app = Flask(__name__)


@app.route('/')
def test_api():

    return render_template('test.html')


# Зарегистрировать компоненты
app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)


# Запуск
app.run()