from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    user_name = models.CharField(unique=True ,max_length=15, null=False, blank=False)
    password = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(unique=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    gender = models.BooleanField(default=True)
    age = models.IntegerField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    registered_time = models.DateTimeField(auto_created=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user_name


class Article(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    caption = models.CharField(max_length=100, blank=False)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class Content(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    is_private = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.caption


class Comment(models.Model):
    writer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="writer")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="commented_content")
    text = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    liker = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="liker")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="liked_content")
    date = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    Rater = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="rater")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="rated_content")
    rate = models.IntegerField(null=False, blank=False)









