from django.db import models

class Research(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    researcher = models.ForeignKey('Researcher', on_delete=models.CASCADE, related_name='researches')

    def __str__(self):
        return self.title
    
class Researcher(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    research = models.ManyToManyField(Research, blank=True, related_name='researchers')

    def __str__(self):
        return self.name
    
class Publication(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    publication_date = models.DateField()
    research = models.ForeignKey(Research, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
