from django.urls import path
from blog.views import post_list_view,post_detail,PostListView
app_name='blog'
urlpatterns = [
    # path('',post_list_view,name="post_list_view"),
    path('<int:id>/', post_detail, name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]
