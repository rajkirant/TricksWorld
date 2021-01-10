from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Software
from django.shortcuts import render
#from django.core import serializers


def software(request):
    softs = Software.objects.all()
    #post_list = serializers.serialize('json', softs)
    #return HttpResponse(post_list, content_type="text/json-comment-filtered")
    return render(request, "software.html",{'softs':softs})

# Create your views here.
class BaseView(TemplateView):
    template_name = 'base.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class GamesView(TemplateView):
    template_name = 'games.html'

class FunView(TemplateView):
    template_name = 'fun.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

@method_decorator(csrf_exempt, name='dispatch')
class ResultView(TemplateView):
    def post(self, request, *args, **kwargs):
        return HttpResponse('result<h1>Mail Sent</h1><br/><br/><br/><br/>Message has been sent.we will contact you soon.')
