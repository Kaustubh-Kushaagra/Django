from django.urls import path
from blog.views import post_list_view,post_detail,PostListView
from . import views
app_name='blog'
urlpatterns = [
    # path('',post_list_view,name="post_list_view"),
    path('<int:id>/', post_detail, name='post_detail'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]
