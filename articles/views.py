from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import CommentForm
from .models import Article
from django.urls import reverse, reverse_lazy


class ArticleListView(ListView):
    model = Article
    template_name = "article/list.html"

    def get_queryset(self):
        queryset = Article.objects.select_related("author").order_by("-date")
        self.selected_category = self.request.GET.get("category", "")
        if self.selected_category in dict(Article.CATEGORY_CHOICES):
            queryset = queryset.filter(category=self.selected_category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = list(context["object_list"])
        context["featured_article"] = articles[0] if articles else None
        context["headline_articles"] = articles[1:5]
        context["remaining_articles"] = articles[5:] if len(articles) > 5 else articles[1:]
        context["category_choices"] = Article.CATEGORY_CHOICES
        context["selected_category"] = self.selected_category
        context["selected_category_label"] = dict(Article.CATEGORY_CHOICES).get(
            self.selected_category, ""
        )
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/detail.html"

    def get_queryset(self):
        return Article.objects.select_related("author").prefetch_related("comments__author")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = kwargs.get("comment_form", CommentForm())
        context["comment_list"] = self.object.comments.select_related("author").order_by("-id")
        same_category_articles = list(
            Article.objects.select_related("author")
            .filter(category=self.object.category)
            .exclude(pk=self.object.pk)
            .order_by("-date")[:6]
        )
        if len(same_category_articles) < 6:
            extra_articles = list(
                Article.objects.select_related("author")
                .exclude(pk=self.object.pk)
                .exclude(category=self.object.category)
                .order_by("-date")[: 6 - len(same_category_articles)]
            )
            same_category_articles.extend(extra_articles)
        context["latest_articles"] = same_category_articles
        context["category_choices"] = Article.CATEGORY_CHOICES
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, "Izohingiz yuborildi.")
            return redirect("detail", pk=self.object.pk)

        return self.render_to_response(
            self.get_context_data(object=self.object, comment_form=form)
        )


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("category", "title", "summary", "body", "photo")
    template_name = "article/update.html"
    success_url = reverse_lazy("list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article/delete.html"
    success_url = reverse_lazy("list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = "article/create.html"
    fields = ("category", "title", "summary", "body", "photo")
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
