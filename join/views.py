from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from . import models,forms
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import timezone


class JobListView(ListView):
    model = models.job_offer

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def job_list(request):
    offers_list = (models.job_offer).objects.order_by('publication_date').reverse() #ordered from the most recent to the less recent.
    return HttpResponse(render(request, 'join/job_list.html', {'offers_list' : offers_list, }))

    
class JobDescription(DetailView):
    model = models.job_offer


def job_description(request, slug):
    job = get_object_or_404(models.job_offer, slug=slug)
    jo = (models.job_offer).objects.filter(slug=slug)
    return HttpResponse(render(request, 'join/job_description.html'.format(slug), {'job' : job, 'jo' : jo, }))


def upload_file(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = models.uploadcv.objects.get(pk=request.FILES['docfile'])
            newdoc.save()
            
            return HttpResponseRedirect(reverse('join.views.upload_file'))
    else:
        form = forms.UploadFileForm()
    
    documents = (models.uploadcv).objects.all()
    return HttpResponse(render(request, 'join/job_description.html', {'documents': documents, 'form': form, }, context_instance=RequestContext(request)))