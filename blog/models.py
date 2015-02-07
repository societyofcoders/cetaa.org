from django.db import models
from django.core.urlresolvers import reverse
from user.models import User

CHOICES = (
	(1,'Upvote'),
	(-1,'Downvote'),
	(0, 'Not Specified')
)

POST_STATUS = {
	(0, 'Saved as Draft'),
	(1, 'Sub Editor Stage'),
	(2, 'Editor Stage'),
	(3, 'Published'),
	(-1, 'Rejected')
}


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=3)

class Post(models.Model):
    title = models.CharField(max_length=200)
    uid = models.ForeignKey(User)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=POST_STATUS)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created"]

class Comment(models.Model):
	post_id = models.ForeignKey(Post)
	uid = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	vote = models.IntegerField(max_length=1,choices=CHOICES)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"
  		ordering = ["-date"]

class Label(models.Model):
	label = models.CharField(max_length=100)

	def __str__(self):
		return self.label

class PostLabels(models.Model):
	post_id = models.ForeignKey(Post)
	label_id = models.ForeignKey(Label)

	class Meta:
		verbose_name = "Posts - Labels"
		verbose_name_plural = "Posts - Labels"
  		ordering = ["-post_id"]