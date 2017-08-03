from django.db import models

# Create your models here.
class Topping(models.Model):
	"""比萨店的模型"""
	text = models.CharField(max_length=100)
	date_added= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Pizza(models.Model):
	"""学习主题的具体知识"""
	pizza = models.ForeignKey(Topping)
	name = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta():
		verbose_name_plural= 'pizzas'

	def __str__(self):
		
		if len(self.name)>50:
			return self.name[:50]+"..."
		else:
			return self.name
