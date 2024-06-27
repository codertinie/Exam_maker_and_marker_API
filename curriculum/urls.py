from django.urls import path
from .views import CurriculumListView, LessonListView, DocumentListView

urlpatterns = [
    path('curricula/', CurriculumListView.as_view()),
    path('curricula/<int:curriculum_id>/lessons/', LessonListView.as_view()),
    path('lessons/<int:lesson_id>/documents/', DocumentListView.as_view()),
]