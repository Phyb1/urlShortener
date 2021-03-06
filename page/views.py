from django.shortcuts import render
from . models import Link
from .forms import LinkForm
from django.http import Http404, HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            link = Link.objects.get(id=6) # getting one fixed result
            url = link.short
            '''or
            newLink =form.save(commit=False)
            newLink.save()
            url = newLink.short
            '''
            form=LinkForm()
            context = {'url': url, 'form':form}
        return render(request, 'page/index.html', context)
    else:
        form = LinkForm()
        context = {'form':form}
        return render(request, 'page/index.html', context)

def about(request):
    return render(request, 'page/about.html')

def result(request, id):
    link = Link.objects.get(keys=id)
    originalLink = link.name
    return HttpResponseRedirect(originalLink)
    