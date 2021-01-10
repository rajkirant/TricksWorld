from django.contrib import admin
from django.urls import path, include
from apps.base.views import BaseView, HomeView, GamesView, FunView, ContactView, AboutView, ResultView
from apps.base import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include(urls)),

    path('', BaseView.as_view(), name='base'),
    path('home/', HomeView.as_view(), name='home'),
    path('games/', GamesView.as_view(), name='games'),
    path('fun/', FunView.as_view(), name='fun'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view()),
    path('result/', ResultView.as_view(), name='dispatch'),



]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
