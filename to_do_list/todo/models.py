from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
	TODO = 'todo'
	DONE = 'done'

	STATUS_CHOICES = (
		(TODO,'Todo'),
		(DONE,'DOne')
	)

	title = models.CharField(max_length=255)
	details = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default=TODO)

	def __str__(self):
		return self.title

