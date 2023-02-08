from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.cvent.com/sites/default/files/styles/focus_scale_and_crop_800x450/public/migrated_attachments/meal-918638_1280-1.jpg?itok=dMJGxEC2")
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    