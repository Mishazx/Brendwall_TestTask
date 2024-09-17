from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
class ClearProductsView(generics.DestroyAPIView):
  def delete(self, request, *args, **kwargs):
      Product.objects.all().delete()
      return Response({'message': 'Все продукты успешно удалены.'}, status=status.HTTP_204_NO_CONTENT)
 

def index(request):
    return render(request, 'products/index.html')
