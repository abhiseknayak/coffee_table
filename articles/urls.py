
from django.conf.urls import url
from django.contrib import admin
from .import views

app_name="articles"

urlpatterns = [
    url(r'^$',views.articles_list,name="list"),
    url(r'^(?P<slug>[\w-]+)/$',views.article_details,name="details"),

]
