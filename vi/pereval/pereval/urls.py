from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Pereval API",
        default_version='v1',
        description="Pereval API предоставляет возможность добавления и редактирования"
                    "информации о туристических перевалах."
                    "Пользователи могут отправлять данные о новых перевалах через мобильное приложение,"
                    "а модераторы ФСТР проводят модерацию и управляют статусами записей."
                    "Цели API: Упрощение процесса добавления и редактирования данных о туристических перевалах."
                    "Создание централизованной системы для хранения и управления информацией о перевалах."
                    "Группы пользвателей: Туристы: Могут отправлять информацию о новых перевалах"
                    "Модераторы ФСТР: Осуществляют модерацию отправленных данных и управляют статусами."
                    "Цели достижения: Повышение удобства для туристов при добавлении информации о перевалах."
                    "Обеспечение централизованного и эффективного контроля за данными о перевалах модераторами ФСТР.",
    ),
    public=True,
    permission_classes=[AllowAny]
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pereval_app.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
