import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import add_post
from loader.utils import save_picture, is_picture

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=['POST'])
def new_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        logging.info('Загруженный файл - не картинка')
        return "Нет картинки или текста"

    if not is_picture(picture):
        return 'Файл не является картинкой'

    path = '/' + save_picture(picture)

    try:
        post = add_post({'pic': path, 'content': content})
    except FileNotFoundError:
        logging.error('Ошибка при загрузке файла')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Ошибка в файле'

    return render_template('post_uploaded.html', post=post)


