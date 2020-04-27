from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify

import os


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    objects = models.Manager()  # Our default Manager
    published = PublishedManager()  # Custom Model Manager

    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    restrict_comment = models.BooleanField(default=False)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    url_address = models.URLField(max_length=300, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("web:post_detail", args=[self.id, self.slug])


@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profile_pictures')

    def _str_(self):
        return "Profile of user {}".format(self.user.username)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#
# @receiver(pre_save, sender=Profile)
# def delete_file_on_change_extension(sender, instance, **kwargs):
#     if instance.pk:
#         try:
#             old_avatar = sender.objects.get(pk=instance.pk).photo
#         except sender.DoesNotExist:
#             return
#         else:
#             new_avatar = instance.photo
#             if old_avatar.url != new_avatar.url:
#                 old_avatar.delete(save=False)


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def _str_(self):
        return self.post.title + "Image"


class Files(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files', blank=True, null=True)
    cover = models.ImageField(upload_to='files/covers/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('web:update_file', kwargs={'pk': self.pk})

    def _str_(self):
        return self.post.title + "Files"


# @receiver(post_delete, sender=Images)
# def deleted_file_delete(sender, instance, **kwargs):
#     if instance.image:
#         if os.path.isfile(instance.image.path):
#             os.remove(instance.image.path)


# @receiver(pre_save, sender=Images)
# def delete_profile_old(sender, instance, **kwargs):
#     if not instance.pk:
#         return False
#     try:
#         old_file = sender.objects.get(pk=instance.pk).image
#     except sender .DoesNotExist:
#         return False
#
#     new_file = instance.image
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name="replies")
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))


























