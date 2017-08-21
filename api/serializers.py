from rest_framework import serializers
from .models import Bucketlist
from .models import RetailersOutletDetails
from .models import RechargeAmount

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
        
class PromotionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = RechargeAmount
        fields = ('id', 'promotionText', 'moneyAmount', 'valid')
        #read_only_fields = ('date_created', 'date_modified')
        
class RetailersSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = RetailersOutletDetails
        fields = ('id', 'shopName', 'latitude', 'longitude','shopCategory','shopAddress','shopMobileNumber','shopServiceList')
        #read_only_fields = ('date_created', 'date_modified')
