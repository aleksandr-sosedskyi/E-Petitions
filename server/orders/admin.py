from django.contrib import admin

from orders import models


admin.site.register(models.Order)
