from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from api_v1.models import Quote
from api_v1.serializers import QuoteSerializer


class QuoteView(APIView):
    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class QuoteViewPK(APIView):
    def put(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=kwargs.get('pk'))
        serializer = QuoteSerializer(data=request.data, instance=quote)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=kwargs.get('pk'))
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=kwargs.get('pk'))
        quote_pk = quote.pk
        quote.delete()
        return Response({
            "message": f"Quote with id {quote_pk} has been deleted."
        }, status=204)