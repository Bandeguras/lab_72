from api_v1.models import Quote
from api_v1.serializers import QuoteSerializer
from rest_framework import generics


class QuoteView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteViewPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

