from django.db import models
from django.contrib.auth import get_user_model

class Memo(models.Model):
    content = models.CharField(max_length=2000)
    update_datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'id=' + str(self.id) + ', update_datetime=' + str(self.update_datetime)
