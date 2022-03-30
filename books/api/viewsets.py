from rest_framework import viewsets
from books.api import serializers
from books import models

from rest_framework.permissions import IsAuthenticated


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()

# user ser salvo automaticamente
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class UsersViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    serializer_class = serializers.UsersSerializer
    queryset = models.Users.objects.all()