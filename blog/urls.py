from django.urls import path
from blog.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
