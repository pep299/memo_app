from django.db import models

class Memo(models.Model):
    content = models.CharField(max_length=2000)
    update_date = models.DateField()

    def __str__(self):
        return 'id=' + str(self.id) + ', update_date=' + str(self.update_date)
