from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),

    path('blogs/', views.blogs, name="blogs"),
    path('create-blog/', views.createBlog, name="create-blog"),
    path('blog/<str:pk>/', views.blogDetail, name="blog"),
    path('upload-blog-media/', views.upload_blog_media, name="upload-blog-media"),
    path('room/<str:pk>/add-resource/', views.addResource, name="add-resource"),
    path('room/<str:pk>/resources/', views.roomResources, name="room-resources"),
]
