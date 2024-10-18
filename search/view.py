from itertools import product
from django.views.generic import ListView
from django.db.models import Q


class SearchResultsView(ListView):
    model = product
    template_name = 'mainpage/search-product.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        products=product.objects.filter(Q(name__icontains=query))
        return products