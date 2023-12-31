from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
]

queryset = Shops.objects.all()

categories_by_shop = []

for shop in queryset:
    categories = Categories.objects.filter(products__shop=shop.pk).distinct()
    categories_by_shop.append((shop, categories))


class DataMixin:
    paginate_by = 20
    model = Shops

    def get_main_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        context["categories_by_shop"] = categories_by_shop
        return context
