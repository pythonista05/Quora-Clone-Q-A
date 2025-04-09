from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post_question/', views.post_question, name='post_question'),
    path('get_question_detail/<int:id>', views.get_question_detail, name='get_question_detail'),
    path('like_answer/<int:id>', views.like_answer, name='like_answer'),
]
