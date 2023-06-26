from flask import Blueprint

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')


@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_comment(post_id: int):
    pass


@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods=['POST'])
def publish_comment(post_id: int, comment_user_id: int):
    pass


@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['PUT'])
def change_comment(comment_id: int, comment_user_id: int):
    pass


@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['DELETE'])
def delete_comment(comment_id: int, comment_user_id: int):
    pass

