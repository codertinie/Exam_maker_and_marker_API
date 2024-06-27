# curriculum/serializers.py
from rest_framework import serializers
from .models import Curriculum, Lesson, Document

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('id', 'title', 'description', 'subject', 'gradeLevel', 'teacher')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'curriculum')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name', 'file', 'lesson')