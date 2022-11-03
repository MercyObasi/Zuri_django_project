from . import views
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('artistes/', views.artiste),
    path('songs/', views.SongView.as_view()),
    path('lyrics/', views.LyricView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('artistes/<int:pk>', views.artiste_detail),
    path('songs/<int:pk>', views.SongDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)