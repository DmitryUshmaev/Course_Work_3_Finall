import json
from json import JSONDecodeError
from bp_posts.dao.post import Post
from exceptions.data_exceptions import DataSourceError


class PostDAO:

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

    def _load_posts(self):
        """
        Возвращает список экземпляров Post
        :return:
        """
        posts_data = self._load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]

        return list_of_posts

    # Все

    def get_all(self):
        """
        Получаем все посты
        :return: Список экземпляров класса Post
        """
        posts = self._load_posts()

        return posts

    # PK

    def get_by_pk(self, pk):
        """
        Получает пост по его РК
        :param pk:
        :return:
        """
        if type(pk) != int:
            raise TypeError("pk must be int")

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    # Поиск

    def search_in_content(self, substring):
        """
        Ищет посты, где в content встречается substring
        :param substring:
        :return:
        """
        if type(substring) != str:
            raise TypeError("substring must be str")

        substring = str(substring).lower()

        posts = self._load_posts()

        matching_posts = [post for post in posts if substring in post.content.lower()]

        return matching_posts

    # Пользователь

    def get_by_poster(self, username):
        """
        Ищет посты конкретного пользователя
        :param username:
        :return:
        """
        if type(username) != str:
            raise TypeError("username must be str")

        user_name = str(username).lower()

        posts = self._load_posts()

        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]

        return matching_posts
