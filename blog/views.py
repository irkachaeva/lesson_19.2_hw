from blog.models import Blog
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from pytils.translit import slugify


class BlogListView(ListView):
    model = Blog
    success_url = reverse_lazy('blog:view')

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = 'title', 'body', 'image'
    success_url = reverse_lazy('blog:view')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'image',)  # Поля для редактирования

    # success_url = reverse_lazy('blog:list')  # Адрес для перенаправления после успешного редактирования

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:view')  # Адрес для перенаправления после успешного удаления



