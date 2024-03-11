from django.contrib import admin
from django.urls import path
from imageboard import urls as board_urls
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(board_urls, namespace='board_feed'))
]
