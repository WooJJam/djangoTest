from django.urls import path

from study import views

app_name = "study"

urlpatterns = [
    path('register/', views.register),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    # path('')
    # path('kakaoLoginLogic/', views.kakaoLoginLogic)
]