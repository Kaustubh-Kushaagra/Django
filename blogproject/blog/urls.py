from django.urls import path
from blog.views import post_list_view,post_detail,PostListView,post_share,post_comment
from django.urls import path
from . import views   # ✅ THIS LINE IS MISSING
app_name='blog'
urlpatterns = [
    #path('',post_list_view,name="post_list_view"),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
]