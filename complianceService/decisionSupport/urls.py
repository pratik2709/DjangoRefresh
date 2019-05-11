from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PollView.as_view()),
]