from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		txt = ""
		words = self.body.split()
		for i in range(10):
			if i >= len(words):
				break
			txt += words[i]+' '
		if i < len(words):
			txt+='....'
		return txt


	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

