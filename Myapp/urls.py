from django.contrib import admin
from django.urls import path
from Myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginuser, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('index', views.index, name="index"),
    path('register', views.register, name="register"),
    path('ask', views.Ask, name="Ask"),
    path('<int:question_id>/ques_ans', views.ques_ans, name="ques_ans"),
]
