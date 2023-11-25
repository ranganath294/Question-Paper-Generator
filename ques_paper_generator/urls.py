from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_routes, name='get_routes'),
    path('generate_question_paper', views.generate_question_paper, name='generate_question_paper'),
    path('create_question', views.create_question, name='create_question'),
]

