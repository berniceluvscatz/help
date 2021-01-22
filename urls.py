from django.urls import path
from . import views


from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('happy', views.Happy, name='happy'),
    path('average', views.Average, name='average'),
    path('sad', views.Sad, name='sad'),
    path('scale', views.Scale, name='scale'),
    path('search/', views.Search, name='search'),
    path('search1/', views.Search1, name='search1'),
    path('search2/', views.Search2, name='search2'),


    ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
