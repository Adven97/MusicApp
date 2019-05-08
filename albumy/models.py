from django.db import models
from datetime import datetime

class Album(models.Model):

    artist = models.CharField(max_length=240)
    album_name = models.CharField(max_length=240)
    year = models.IntegerField(default=1969)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albumy"

    def __str__(self):
        return self.album_name +' by '+self.artist

    # def get_absolute_url(self):
    #     return reverse("Album_detail", kwargs={"pk": self.pk})

class UserData(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    nick = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Posts(models.Model):
    title = models.CharField(max_length=240)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posty"
