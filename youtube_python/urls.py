
from youtube.views import Homeview,newvideo,loginview,registerview,ChannelView,LogoutView,VideoView,LorDView,subview,subscribtions_View
from django.contrib import admin
from youtube import views

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django_email_verification import urls as email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homeview.as_view()),
    path('newvideo/',newvideo.as_view()),
    path('login/',loginview.as_view()),
    path('register/',registerview.as_view()),
    path('logout/',LogoutView.as_view()),
    path('subscribtions/',subscribtions_View.as_view()),
    path('video/<int:id>/',VideoView.as_view()),
    path('channel/',ChannelView.as_view()),
    path('sub/<int:Vid>/<int:id>/',subview.as_view()),
    path('like/<int:lord>/<int:id>/',LorDView.as_view()),
    path('email/', include(email_urls)),	
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)