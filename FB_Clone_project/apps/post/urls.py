
from django.urls import path
from .views import *
app_name = "Post"
urlpatterns = [
    path('post/', PostFormView, name= 'post'),
    path('dashbord/', dashbord, name= 'dashbord'),
    path('all_user_post/', all_user_post, name= 'all_user_post'),
    path('view_post/', view_post, name= 'view_post'),
    path('update_post/<int:id>/', update_post, name= 'update_post'),
    path('delete_post/<int:id>/', delete_post, name= 'delete_post'),
    
    
    path('post_detail/<int:post_id>', post_detail, name= 'post_detail'),
    
    path('post/comment/<int:post_id>/', comment_on_post, name='comment_on_post'),
]
