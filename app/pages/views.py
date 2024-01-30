# from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Blog, Category, Tag


# Create your views here.
# class HomePageView(TemplateView):
#     template_name = "home.html"

# def index(request):
#     blogs = Blog.objects.order_by('-id')
#     return render(request, 'index.html', {'blogs': blogs})


# def detail(request, blog_id):
#     blog_tex = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'detail.html', {'blog': blog_tex})

class IndexView(ListView):
    model = Blog
    context_object_name = "blog_list"
    template_name = 'pages/index.html'

    def get_queryset(self):
        queryset = Blog.objects.order_by('-id')
        return queryset


class CategoryView(ListView):
    """カテゴリー一覧"""
    model = Blog
    context_object_name = "blog_list"
    template_name = 'pages/index.html'

    def get_queryset(self):
        """カテゴリーで絞り込み"""
        category = Category.objects.get(name=self.kwargs['category'])
        queryset = Blog.objects.order_by('-id').filter(category=category)
        return queryset


    def get_context_data(self, **kwargs):
        """テンプレートに渡す辞書の作成"""
        context = super().get_context_data(**kwargs)
        context['category_key'] = self.kwargs['category']
        return context


class TagView(ListView):
    """タグ一覧"""
    model = Blog
    context_object_name = "blog_list"
    template_name = 'pages/index.html'

    def get_queryset(self):
        """タグで絞り込み"""
        tag = Tag.objects.get(name=self.kwargs['tag'])
        queryset = Blog.objects.order_by('-id').filter(tag=tag)
        return queryset


    def get_context_data(self, **kwargs):
        """テンプレートに渡す辞書の作成"""
        context = super().get_context_data(**kwargs)
        context['tag_key'] = self.kwargs['tag']
        return context


class DetailView(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = 'pages/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(pk=self.kwargs['pk'])
        return context
