from django.db import models
from django.utils import timezone


class Issue(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField(null=False)
    image=models.ImageField(upload_to='images/')
    date=models.DateTimeField('date published', default = timezone.datetime.now())
    writer=models.CharField(max_length=50)
    key=models.CharField(max_length=50)

    def summary(self):
        return self.body[:50]

    # class Meta:
    #     model = Issue        
    #     fields = ['key']
    #     widgets = {
    #         'key' : forms.Select()
    #     }

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null = True, related_name='comments')
    contents = models.CharField(max_length=500)
    com_writer=models.CharField(max_length=50, default = "default")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.contents