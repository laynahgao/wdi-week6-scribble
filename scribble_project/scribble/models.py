from django.db import models

# Create your models here.
class Post(models.Model):
  author = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=300)

  def __str__(self):
        return self.author

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  author = models.CharField(max_length=100)
  body = models.CharField(max_length=300)

  def __str__(self):
        return self.author
