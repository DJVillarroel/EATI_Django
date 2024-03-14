from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView

app_name = 'imageboard'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('createpost/', AddPostView.as_view(), name='create_post'),
]

