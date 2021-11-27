from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from django.core.mail import EmailMessage, get_connection
from django_filters import rest_framework as filters
from .filters import UserFilter
from .models import User
from .serializers import UserSerializer
from PIL import Image
import uuid
from test_task import settings
from django.http import JsonResponse
from django.contrib.auth import login


class ListCreateUser(ListCreateAPIView):
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    def get_queryset(self):
        queryset = User.objects.all().exclude(username=self.request.user.username)
        return queryset

    def perform_create(self, serializer):
        obj = serializer.save()
        image = Image.open(obj.avatar)
        watermark = Image.open(settings.MEDIA_ROOT + '/assets/Sample-Watermark-Transparent.png')
        filename = f'/media/{uuid.uuid4()}.png'
        width, height = image.size
        resized_watermark = watermark.resize((width, height), Image.ANTIALIAS)
        transparent_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        transparent_image.paste(image, (0, 0))
        transparent_image.paste(resized_watermark, (0, 0), mask=resized_watermark)
        transparent_image.save(settings.MEDIA_ROOT + filename)
        obj.avatar = filename
        obj.save()
        login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')


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
