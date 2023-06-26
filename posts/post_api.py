from flask import Blueprint


post_bp = Blueprint('user_posts', __name__, url_prefix='/post')


# Получить все посты
@post_bp.route('/', methods=['GET'])
def get_all_user_posts():
    pass


# Получить определенный пост
@post_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post(post_id: int):
    pass


@post_bp.route('/<int:user_id>/<int:post_id>', methods=['PUT'])
def change_user_post(user_id: int, post_id: int):
    pass


@post_bp.route('/<int:user_id>/<int:post_id>', methods=['DELETE'])
def delete_user_post(user_id: int, post_id: int):
    pass


# Опублиуковать пост
@post_bp.route('/upload_post', methods=['POST'])
def create_post(post_text: str, post_photo: str, hashtags: list, user_id: int):
    pass


