from django.db import models
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='Title')
    contents = models.TextField(verbose_name='Contents')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='Writer')
    tags = models.ManyToManyField('tag.Tag', verbose_name='Tag')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='Written Date')
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'compass_ask_board'
        verbose_name = 'compass ask board'
        verbose_name_plural = "compass ask boards"