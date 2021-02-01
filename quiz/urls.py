from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


quiz_router = DefaultRouter()
quiz_router.register(r'quizes', views.QuizViewset)
comment_router = DefaultRouter()
comment_router.register(r'comments', views.CommentViewset)

api = [
    path('', quiz_router),
    path('quizes/<int:quiz_pk>', comment_router)
]

urlpatterns = [
    include(api),
]

