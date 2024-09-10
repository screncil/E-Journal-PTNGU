from django.urls import path

from .views import TokenExistsView


urlpatterns = [
    path('/exists', TokenExistsView.as_view(), name='token-exists'),
]