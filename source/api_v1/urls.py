from django.urls import path, include
from api_v1.views import QuoteView, QuoteViewPK

app_name = 'api_v1'

QuoteUrl = [
    path('', QuoteView.as_view()),
    path('<int:pk>/', QuoteViewPK.as_view()),
]

urlpatterns = [
    path('quote/', include(QuoteUrl)),
]
