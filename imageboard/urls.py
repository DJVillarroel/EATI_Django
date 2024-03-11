from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, PostDetailView

app_name = 'imageboard'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    #path('post/', AddPostView.as_view(), name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)