from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .data_manager import DataManager
from .serializers import PerevalSerializer
from .models import PerevalAdded


class SubmitDataView(APIView):
    """
        Этот API-метод предназначен для получения информации о конкретном перевале.

    Parameters:
    - `beauty_title` (str): Красивое название перевала.
    - `title` (str): Название перевала.
    - `other_titles` (str): Дополнительные названия перевала.
    - `connect` (str): Дополнительная информация о перевале.
    - `level_winter` (str, optional): Уровень сложности зимой.
    - `level_summer` (str, optional): Уровень сложности летом.
    - `level_autumn` (str, optional): Уровень сложности осенью.
    - `level_spring` (str, optional): Уровень сложности весной.
    - `latitude` (float): Широта перевала.
    - `longitude` (float): Долгота перевала.
    - `height` (int): Высота перевала.
    - `email` (str): Email пользователя.
    - `fam` (str): Фамилия пользователя.
    - `name` (str): Имя пользователя.
    - `otc` (str): Отчество пользователя.
    - `phone` (str): Номер телефона пользователя.

    Returns:
    - `status` (int): Статус операции (200 - успешно, 404 - перевал не найден).
    - `message` (str): Сообщение об операции.
    - `id` (int): Идентификатор нового перевала.
        """

    @staticmethod
    def post(request):
        data = request.data

        try:
            pereval_id = DataManager.add_pereval(data)
            return Response({'status': 200, 'message': None, 'id': pereval_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status': 500, 'message': str(e), 'id': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def patch(request, pereval_id):
        # Получаем перевал
        pereval = get_object_or_404(PerevalAdded, id=pereval_id)

        # Проверяем, что статус "new"
        if pereval.status != 'new':
            return Response({'state': 0, 'message': 'Cannot edit object with status other than "new"'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Определяем поля, которые нельзя редактировать
        protected_fields = ['fam', 'name', 'otc', 'email', 'phone', 'status']

        # Получаем обновляемые данные, исключая защищенные поля
        update_data = {key: value for key, value in request.data.items() if key not in protected_fields}

        try:
            # Применяем обновления, если есть что обновлять
            if update_data:
                PerevalAdded.objects.filter(id=pereval_id).update(**update_data)
            return Response({'state': 1, 'message': None}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'state': 0, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetPerevalView(APIView):
    """
    Этот API-метод предназначен для получения информации о конкретном перевале.

    Parameters:
    - `pereval_id` (int): Идентификатор перевала.

    Returns:
    - `status` (int): Статус операции (200 - успешно, 404 - перевал не найден).
    - `message` (str): Сообщение об операции.
    - `data` (dict): Информация о перевале, включая статус модерации.
    """

    @staticmethod
    def get(_, pereval_id):
        # Получаем перевал
        pereval = get_object_or_404(PerevalAdded, id=pereval_id)

        # Получаем статус модерации
        moderation_status = pereval.status

        # Сериализуем данные
        serializer = PerevalSerializer(pereval)

        # Добавляем статус модерации в данные
        data_with_status = {
            'status': moderation_status,
            'data': serializer.data
        }

        return Response(data_with_status, status=status.HTTP_200_OK)


class UserPerevalsView(ListAPIView):
    """
    Этот API-метод предназначен для просмотра всех объектов, когда-либо отправленных на сервер пользователем,
    а также их статусов.

    Parameters:
    - `user__email` (str): Email пользователя.

    Returns:
    - `status` (int): Статус операции (200 - успешно).
    - `message` (str): Сообщение об операции.
    - `data` (list): Список объектов, отправленных пользователем, включая их статусы.
    """

    serializer_class = PerevalSerializer

    def get_queryset(self):
        # Получаем email пользователя из параметров запроса
        user_email = self.request.query_params.get('user__email', '')

        # Фильтруем объекты по email пользователя
        queryset = PerevalAdded.objects.filter(user__email=user_email)

        return queryset

    def list(self, request, *args, **kwargs):
        # Получаем список объектов
        queryset = self.get_queryset()

        # Сериализуем список объектов
        serializer = PerevalSerializer(queryset, many=True)

        # Создаем список объектов с добавленным статусом модерации
        data_with_status = [{'status': obj.status, 'data': serialized_data} for obj, serialized_data in
                            zip(queryset, serializer.data)]

        # Возвращаем результат
        return Response(data_with_status, status=status.HTTP_200_OK)
