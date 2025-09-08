from django.contrib import admin
from .models import CapturedRequests,CapturedResponses

# Register your models here.
admin.site.register(CapturedResponses)
admin.site.register(CapturedRequests)
