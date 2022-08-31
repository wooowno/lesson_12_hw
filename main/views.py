import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import get_posts_by_tag

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    tag = request.args.get('s', '')

    logging.info('Выполняется поиск')

    try:
        posts = get_posts_by_tag(tag)
    except FileNotFoundError:
        logging.error('Ошибка при загрузке файла')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Ошибка в файле'

    return render_template("post_list.html", tag=tag, posts=posts)
