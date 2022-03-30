from django.db import models
from uuid import uuid4

from django.contrib import auth
from django.contrib.auth.models import User

from django.conf import settings


def upload_image_books(instance, filename):
    return f"{instance.id_book}-{filename}"


class Books(models.Model):

    STATE_CHOICES = (
        ("new", "novo"),
        ("old", "velho"),
        ("uso", "usado"),
        ("lixo", "só o resto")
    )

    #criando os atributos do livro
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=4, default="sem info", choices=STATE_CHOICES, blank=False, null=False)
    image = models.ImageField(upload_to=upload_image_books, blank=False, null=True)

    # user = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
    # ValueError: Cannot assign "<User: pauloadmendonca>": "Books.user" must be a "Users" instance.

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # from django.contrib.auth.models import User ---> função user do django

    def __str__(self):
        return self.title

    
class Users(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
