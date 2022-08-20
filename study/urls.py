from django.urls import path
from study.views import center_sort

app_name = "accountapp"

urlpatterns = [
    path('center_sort/', center_sort,name="center_sort")
]