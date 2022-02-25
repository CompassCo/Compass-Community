from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='tag name')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'compass_tag'
        verbose_name = 'Compass tag'
        verbose_name_plural = 'Compass tags'
