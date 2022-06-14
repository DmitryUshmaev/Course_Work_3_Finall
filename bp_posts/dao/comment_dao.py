import json
from json import JSONDecodeError

from bp_posts.dao.comment import Comment
from exceptions.data_exceptions import DataSourceError


class CommentDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """
        Загружает данные из json
        :return: Список словарей
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла {self.path}")

        return posts_data

    def _load_comments(self):
        """
        Возвращает список экземпляров Post
        :return:
        """
        comments_data = self._load_data()
        list_of_posts = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_posts

    def get_comments_by_post_pk(self, post_pk):

        comments = self._load_comments()
        comments_match = [comment for comment in comments if comment.post_id == post_pk]
        return comments_match
