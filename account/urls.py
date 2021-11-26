from django.urls import path

from account.views import ListCreateUser, LikePartner

urlpatterns = [
    path('clients/', ListCreateUser.as_view()),
    path('clients/create/', ListCreateUser.as_view()),
    path('clients/<int:pk>/match', LikePartner.as_view())
]
