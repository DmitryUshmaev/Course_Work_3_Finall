from flask import Blueprint, render_template, abort, request

from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from config import DATA_PATH_POST, DATA_PATH_COMMENTS

# Blueprints
bp_posts = Blueprint("bp_posts", __name__, template_folder="templates")

# Объекты DAO
post_dao = PostDAO(DATA_PATH_POST)
comment_dao = CommentDAO(DATA_PATH_COMMENTS)


@bp_posts.route("/")
def page_posts():
    """
    Страница всех постов
    :return:
    """
    all_post = post_dao.get_all()
    return render_template("index.html", posts=all_post)


@bp_posts.route("/post/<int:pk>")
def page_post_single(pk):
    """
    Страница одного поста
    :param pk:
    :return:
    """
    post = post_dao.get_by_pk(pk)
    comments = comment_dao.get_comments_by_post_pk(pk)

    if post is None:
        abort(404)
    return render_template("post.html", post=post, comments=comments)


@bp_posts.route("/users/<user_name>")
def page_posts_by_user(user_name):
    """
    Возвращает посты определенного пользователя
    :param user_name:
    :return:
    """
    posts = post_dao.get_by_poster(user_name)

    if posts == []:
        abort(404, "Такого пользователя не существует")

    return render_template("user-feed.html", posts=posts)

@bp_posts.route("/search/")
def page_posts_search():
    """
    Возвращает результаты поиска
    :return:
    """
    query = request.args.get("s", "")

    if query == "":
        posts = []
    else:
        posts = post_dao.search_in_content(query)

    return render_template("search.html", posts=posts, query=query, posts_len=len(posts))