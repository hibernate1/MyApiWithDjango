from django.shortcuts import render

from rest_framework import generics
from .serializers import BucketlistSerializer, RetailersSerializer
from .serializers import PromotionSerializer
from .models import Bucketlist
from .models import RechargeAmount
from .models import RetailersOutletDetails
from rest_framework.decorators import api_view
from .service import TestBook
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import When, Case, F, IntegerField

class CreateView(generics.ListCreateAPIView ):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
        
        
class PromotionList(generics.ListCreateAPIView):
    
    queryset = RechargeAmount.objects.filter(valid = True).order_by('moneyAmount')
    serializer_class = PromotionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
        
        

class Test(generics.ListCreateAPIView):
    
    queryset = RechargeAmount.objects.all()
    serializer_class = PromotionSerializer

    def get_queryset(self):
        queryset = RechargeAmount.objects.all()
      #  workspace = self.request.query_params.get('PromotionText')
      
        RechargeAmount.objects.filter(valid = True)
      
       # airline = self.request.query_params.get('airline')
        queryset = queryset.filter(PromotionText=workspace)
        return queryset 


@api_view(['GET', 'POST'])
def task_list(request):
 
    if request.method == 'GET':
        return Http ("GET Request.")

    elif request.method == 'POST':
        payment_id = request.POST.get('payment_id', '')
        return HttpResponse(payment_id)
        
    
    
@api_view(['GET', 'POST'])
def getMan(request):
    if request.method == 'GET':
        books_list = TestBook.getbooks()
        return HttpResponse(books_list)   
    
    
class RetailersList(generics.ListCreateAPIView):
    
    queryset = RetailersOutletDetails.objects.filter(valid = True)
    serializer_class = RetailersSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()  
