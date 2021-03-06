from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from django.core.mail import EmailMessage, get_connection
from django_filters import rest_framework as filters
from .filters import UserFilter
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse


class ListCreateUser(ListCreateAPIView):
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    def get_queryset(self):
        queryset = User.objects.all().exclude(username=self.request.user.username)
        return queryset


class LikePartner(APIView):
    def get(self, request, pk):
        recipient = User.objects.get(pk=pk)
        connection = get_connection()
        connection.open()
        email = EmailMessage("Date Site",
                             f"Вы понравились {request.user.username}! Почта участника {request.user.email}",
                             f"{request.user.email}", [recipient.email])
        connection.send_messages([email])
        connection.close()
        return JsonResponse({'data': 'The email has been sent successfully!'})
