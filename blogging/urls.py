#---------------------------------------------------------------------#
# Title: urls.py
# Desc: <Enter Description here>
#---------------------------------------------------------------------#
# 1:53:57
from django.urls import path
from blogging.views import BloggingListView, BloggingDetailView

urlpatterns = [path('', BloggingListView.as_view(), name="blog_index"),
               path('posts/<int:pk>/', BloggingDetailView.as_view(), name="blog_detail"),]
