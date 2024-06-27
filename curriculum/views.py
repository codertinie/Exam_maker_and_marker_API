from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Curriculum, Lesson, Document
from .serializers import CurriculumSerializer, LessonSerializer, DocumentSerializer

class CurriculumListView(APIView):
    def get(self, request):
        curricula = Curriculum.objects.all()
        serializer = CurriculumSerializer(curricula, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CurriculumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonListView(APIView):
    def get(self, request, curriculum_id):
        lessons = Lesson.objects.filter(curriculum_id=curriculum_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def post(self, request, curriculum_id):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(curriculum_id=curriculum_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentListView(APIView):
    def get(self, request, lesson_id):
        documents = Document.objects.filter(lesson_id=lesson_id)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, lesson_id):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(lesson_id=lesson_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)