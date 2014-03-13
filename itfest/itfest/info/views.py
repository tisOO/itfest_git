from django.shortcuts import render

from itfest.info.models import News, Chat

# Create your views here.


def view_news(request, count_news = 5):
	p = News.objects.order_by('-time')[0:count_news]
	return render(request, 'news.html', {'news':p})
	