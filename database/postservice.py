from models import Post, PostPhoto, PostComment, db


# Получить все посты
def get_all_posts_db():
    posts = Post.query.all()
    return posts


# Получить все изображения
def get_all_photo_db():
    photos = PostPhoto.query.all()
    return photos


# Получить определенный пост
def get_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    return post


# Удалить пост
def delete_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        db.session.delete(post)
        db.session.commit()


# Иззменить текст поста
def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        post.post_text = new_text
        db.session.commit()


# Добавить коментарий к посту
def add_comment_post_db(post_id, comment_user_id, comment_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        new_comment = PostComment(post_id=post_id, user_id=comment_user_id, comment_text=comment_text)
        db.session.add(new_comment)
        db.session.commit()
