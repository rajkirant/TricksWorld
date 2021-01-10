from django.urls import path
from . import views
from apps.base.views import BaseView, HomeView, GamesView, FunView, ContactView, AboutView, ResultView
urlpatterns = [
    path('software/', views.software, name='software'),
    path('', BaseView.as_view(), name='base'),
    path('home/', HomeView.as_view(), name='home'),
    path('games/', GamesView.as_view(), name='games'),
    path('fun/', FunView.as_view(), name='fun'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view()),
    path('result/', ResultView.as_view(), name='dispatch'),

    ]