from django.shortcuts import render

#bs
from bs4 import BeautifulSoup
#requests
import requests


# Create your views here.

#ex with FBV

def dj_bs(request):
    if request.method == "POST":

    	#url
        url = request.POST.get('web_link', None)

        #requests
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}#headers
        source= requests.get(url, headers=headers).text # website's source
        
        #beautifulsoup
        soup = BeautifulSoup(source, 'html.parser')
        #check if <h1> element is found
        if soup.h1:
           result = soup.h1.string
        else:
            result = "H1 Element is not found"

        return render(request, 'django-bs.html', {'result':result})

    return render(request, 'django-bs.html')






from django.views.generic import TemplateView

class DjBs(TemplateView):
	template_name = "django-bs.html"

	def post(self, request, *args, **kwargs):

		website_link = request.POST.get('web_link', None)

		#requests
		url = website_link
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}#headers
		source= requests.get(url, headers=headers).text # website's source
		
		#beautifulsoup
		soup = BeautifulSoup(source, 'html.parser')

		#check if <h1> element is found
		if soup.h1:
			result = soup.h1.string
		else:
			result = "H1 Element is not found"

		return render(request, 'django-bs.html', {'result':result})



