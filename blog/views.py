from django.core.urlresolvers import reverse
from .forms import BlogForm
from .models import BlogPost, CategoryToPost
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.views.generic import (DetailView,
                                  ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)


# Create your views here.
class BlogList(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    ordering = ["-timestamp"]

    def get_success_url(self):
        return reverse('blog-list')

class CreateBlogPost(CreateView):
    model = BlogPost
    template_name = 'blogpost_create.html'
    form_class = BlogForm

    def get_success_url(self):
        return reverse('blog-list')

    def get_context_data(self, **kwargs):
        context = super(CreateBlogPost, self).get_context_data(**kwargs)
        context['action'] = reverse('blog-create')
        return context

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.get(username=self.request.user)  # use your own profile here
        candidate.save()
        return HttpResponseRedirect(self.get_success_url())

class BlogUpdate(UpdateView):
    model = BlogPost
    form_class = BlogForm
    template_name = 'blogpost_create.html'

    def get_success_url(self):
        return reverse('blog-list')

    def get_context_data(self, **kwargs):
        context = super(BlogUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('blog-update', kwargs={'slug': self.get_object().slug})
        return context

class BlogDelete(DeleteView):
    model = BlogPost
    form_class = BlogForm
    template_name = 'blogpost_delete.html'

    def get_success_url(self):
        return reverse('blog-list')

class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'

    def get_success_url(self):
        return reverse('blog-detail')


class CategoryList(ListView):
    model = CategoryToPost
    template_name = 'category_list.html'
    ordering = ["-timestamp"]

    def get_success_url(self):
        return reverse('category-list')

class CategoryDetail(DetailView):
    model = CategoryToPost
    template_name = 'category_detail.html'

    def get_success_url(self):
        return reverse('category-detail')
