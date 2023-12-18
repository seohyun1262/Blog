from django.urls import path
from blog import views
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    path("", views.index, name = "index"), # 홈페이지
    path("post/<int:pk>", views.PostDetailView.as_view(), name = "post"), # 게시글
    path("post/create", views.PostCreate.as_view(), name = "post_create"), # 새 글 작성하기 
    path('delete/<str:id>', views.delete, name="delete"), # 삭제하기
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name = "update"),
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/',auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]
