from django.urls import path

from account.views import ListCreateUser, LikePartner

urlpatterns = [
    path('clients/', ListCreateUser.as_view()),  # The url is for both listing and creating users
    path('clients/<int:pk>/match', LikePartner.as_view())
]
