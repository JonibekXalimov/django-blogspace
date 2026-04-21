from django.views.generic import TemplateView
from articles.models import Article

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = list(Article.objects.select_related("author").order_by("-date"))
        context["featured_article"] = articles[0] if articles else None
        context["sidebar_articles"] = articles[1:5]
        context["latest_articles"] = articles[5:11] if len(articles) > 5 else articles[1:7]
        context["category_choices"] = Article.CATEGORY_CHOICES
        category_sections = []
        for key, label in Article.CATEGORY_CHOICES:
            items = [article for article in articles if article.category == key][:4]
            if items:
                category_sections.append(
                    {
                        "key": key,
                        "label": label,
                        "articles": items,
                    }
                )
        context["category_sections"] = category_sections
        return context
