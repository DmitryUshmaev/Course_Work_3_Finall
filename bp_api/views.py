import logging

from flask import Blueprint, jsonify
from flask import Blueprint, render_template, abort, request

from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from config import DATA_PATH_POST, DATA_PATH_COMMENTS

# Объекты DAO
post_dao = PostDAO(DATA_PATH_POST)
comment_dao = CommentDAO(DATA_PATH_COMMENTS)

# Создаем blueprint
bp_api = Blueprint("bp_api", __name__)

api_logger = logging.getLogger("api_logger")

@bp_api.route('/posts/')
def api_posts_all():
    """
    Эндпоинт для всех постов
    :return:
    """
    all_posts = post_dao.get_all()
    api_logger.debug("Запрошены все посты")

    return jsonify([post.as_dict() for post in all_posts]), 200


@bp_api.route('/posts/<int:pk>/')
def api_post(pk):
    """
    Эндпоинт для одного потав
    :param pk:
    :return:
    """
    post = post_dao.get_by_pk(pk)

    if post is None:
        api_logger.debug(f"Обращение к несуществующему посту {pk}")
        abort(404)

    api_logger.debug(f"Обращение к посту {pk}")

    return jsonify(post.as_dict()), 200


@bp_api.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка {error}")
    return jsonify({"error": str(error)}), 404
