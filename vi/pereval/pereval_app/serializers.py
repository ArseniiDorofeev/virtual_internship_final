from rest_framework import serializers
from .models import PerevalAdded


class PerevalSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели PerevalAdded.

        Fields:
        - `id` (int): Идентификатор перевала.
        - `beauty_title` (str): Красивое название перевала.
        - `title` (str): Название перевала.
        - `other_titles` (str): Дополнительные названия перевала.
        - `connect` (str): Дополнительная информация о перевале.
        - `add_time` (datetime): Время добавления перевала.
        - `status` (str): Статус модерации (new, pending, accepted, rejected).
        - `user` (dict): Информация о пользователе.
        - `coords` (dict): Информация о координатах перевала.
        - `level_winter` (str, optional): Уровень сложности зимой.
        - `level_summer` (str, optional): Уровень сложности летом.
        - `level_autumn` (str, optional): Уровень сложности осенью.
        - `level_spring` (str, optional): Уровень сложности весной.
        """

    class Meta:
        model = PerevalAdded
        fields = '__all__'
