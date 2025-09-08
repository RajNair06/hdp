from django.db import models
import requests

# Create your models here.
class CapturedRequests(models.Model):
    method = models.TextField()
    headers = models.JSONField()
    body = models.TextField(null=True, blank=True) 
    forward_url=models.URLField()
    client_ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

class CapturedResponses(models.Model):
        response_status = models.IntegerField(null=True, blank=True)
        response_headers = models.JSONField(null=True, blank=True)
        response_body = models.TextField(null=True, blank=True)
            
    

