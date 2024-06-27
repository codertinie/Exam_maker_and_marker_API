
from django.db import models
from django.conf import settings

class Curriculum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    gradeLevel = models.CharField(max_length=50)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='curriculum_documents')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)