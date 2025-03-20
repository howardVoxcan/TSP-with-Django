from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="index"),  # Gộp xử lý vào 1 URL duy nhất
]
