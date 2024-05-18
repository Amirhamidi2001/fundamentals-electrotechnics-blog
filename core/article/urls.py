from django.urls import path

from article.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
