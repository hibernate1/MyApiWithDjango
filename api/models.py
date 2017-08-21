
from django.db import models

# Create your models here.
from django.db import models
from unittest.util import _MAX_LENGTH

from django import forms


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
    
    
class MyModel(models.Model):
  id = models.AutoField(primary_key=True)
  field1 = models.CharField(max_length=50)
  field2 = models.CharField(max_length=50)

  class Meta:
    unique_together = ('field1', 'field2')
    
    
    
class UserDetails(models.Model):
    id =  models.AutoField(primary_key=True)
    deviceId = models.CharField(max_length=50)
    simSerial = models.CharField(max_length=50)
    msisdn = models.CharField(max_length=32)
    
    class Meta:
        unique_together = ('deviceId','simSerial','msisdn')
    
    

class TokenList(models.Model):
    userDetailId = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    id = models.AutoField(primary_key = True)
    token = models.CharField(max_length=50)
    isTokenalive = models.BooleanField
    class Meta:
        unique_together = ('token',)
        
class TokenUse(models.Model):
    id = models.AutoField(primary_key = True)
    tokenListId = models.ForeignKey(TokenList,on_delete= models.CASCADE)
    lastTimeUsed = models.CharField(max_length=50)
    
    
class OTPList(models.Model):
    id = models.AutoField(primary_key = True)
    UserDetailsId = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    otp = models.CharField(max_length = 10)
    generateTime = models.CharField(max_length = 20)
    numberofTried = models.IntegerField
    otpStatus = models.BooleanField
    
    class Meta:
        unique_together = ('otp',)
        
        
    
class RechargeAmount(models.Model):
    id = models.AutoField(primary_key = True)
    promotionText = models.CharField(max_length = 150)
    moneyAmount = models.IntegerField()
    valid = models.BooleanField()
    
    def __str__(self):
        return '%s                        %s'%(self.promotionText,self.moneyAmount)


class RetailersOutletDetails(models.Model):
    id = models.AutoField(primary_key=True)
    shopName = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    shopCategory = models.CharField(max_length= 20)
    shopAddress = models.CharField(max_length= 150)
    shopMobileNumber = models.CharField(max_length=20)
    shopServiceList = models.CharField(max_length= 700,default="")
    valid = models.BooleanField(default=True)


    def __str__(self):
        return '%s %s %s' % (self.shopName, self.shopAddress, self.shopMobileNumber)
        
    
    




