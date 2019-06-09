from django.db import models

class Memo(models.Model):
    content = models.CharField(max_length=2000)
    update_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'id=' + str(self.id) + ', update_datetime=' + str(self.update_datetime)
