from django.db import models
from django.utils import timezone

# Create your models here.
class CapturedRequests(models.Model):
    method = models.TextField()
    headers = models.JSONField()
    body = models.TextField(null=True, blank=True) 
    forward_url=models.URLField()
    client_ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return f"{self.method} {self.forward_url or 'NO-FORWARD-URL'} at{self.timestamp}"

class CapturedResponses(models.Model):
        response_status = models.IntegerField(null=True, blank=True)
        response_headers = models.JSONField(null=True, blank=True)
        response_body = models.TextField(null=True, blank=True)
        created_at=models.DateTimeField(default=timezone.now)

        def __str__(self):
              return f"Response {self.response_status} at {self.created_at}"
        
class CapturedLogs(models.Model):
      log_entry=models.TextField()
      created_at=models.DateTimeField(default=timezone.now)

      def __str__(self):
            return f"log at {self.created_at}"

            
    

