from django.urls import path

from .views import SubmitDataView

urlpatterns = [
    path('submit_data/', SubmitDataView.as_view(), name='submit_data'),
]
