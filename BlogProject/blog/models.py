#from django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (1,'Publish'),
    (0,'Draft')
)
class Post(models.Model):
    """
    Name: Post 
    Description: This Class stores various Posts for a particular Author
    author: Hyacinthemiamo5@gmail.com
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    """
    Name: Comment 
    Description:This Class stores Comments for related Post 
    author: Hyacinthemiamo5@gmail.com
    """
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
