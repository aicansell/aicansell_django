from django.urls import path

from transaction.views import ListTransactionsView

urlpatterns = [
    path('', ListTransactionsView.as_view(), name='transactions')
]
