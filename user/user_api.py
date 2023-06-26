from flask import Blueprint


user_bp = Blueprint('user', __name__, url_prefix='/user')


# Получить всех пользователей
@user_bp.route('/', methods=['GET'])
def get_all_users():
    pass


# Получить определенного пользователя по user_id
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user(user_id: int):
    pass


# Изменить данные пользователя по user_id
@user_bp.route('/<int:user_id>', methods=['PUT'])
def change_user_info(user_id: int):
    pass


# Удалить страницу пользователя
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_exact_user(user_id: int):
    pass

