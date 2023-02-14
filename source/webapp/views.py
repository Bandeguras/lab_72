from api_v1.models import Quote
from django.views.generic import ListView


class IndexViews(ListView):
    template_name = 'index.html'
    context_object_name = 'quotes'
    model = Quote