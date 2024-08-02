from blog.models import Blog
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog


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
    success_url = reverse_lazy('students:list')  # Адрес для перенаправления после успешного редактирования


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')  # Адрес для перенаправления после успешного удаления