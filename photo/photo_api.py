from flask import Blueprint, request


photo_bp = Blueprint('photo', __name__, url_prefix='/photo')


@photo_bp.route('/', methods=['GET'])
def get_all_photo():
    pass


#Публикация фотографии
@photo_bp.route('/', methods=['POST'])
def save_user_photo():
    # Получить фото из фронт части
    file = request.files.get('image', '')
    file.save('user_photos/'+file.filename)
    print(file)
    return 'hello'


@photo_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user_photos(user_id: int):
    pass


@photo_bp.route('/<int:photo_id>', methods=['GET'])
def get_exact_photo(photo_id: int):
    pass


@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['PUT'])
def change_user_photo(user_id: int, photo_id: int):
    pass


@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['DELETE'])
def delete_user_photo(user_id: int, photo_id: int):
    pass



