from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.models import EmailAddress

import hashlib

# largely swiped from here:
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
# and 
# http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    address = models.CharField(blank=True, max_length=200)
    parcel = models.CharField(blank=True, max_length=50)
    trashpickup = models.CharField(blank=True, max_length=200)

    def __str__(self):
      return str(self.user.username)    

    def account_verified(self):
      """
      If the user is logged in and has verified hisser email address, return True,
      otherwise return False
      """
      result = EmailAddress.objects.filter(email=self.user.email)
      if len(result):
         return result[0].verified
      return False

    def profile_image_url(self):
      """
      Return the URL for the user's Facebook icon if the user is logged in via Facebook,
      otherwise return the user's Gravatar URL
      """

      return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5('epaulson@unit1127.com'.encode('utf-8')).hexdigest())

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# this should really be a core set of stops that is managed by
# the app and then a user has a bunch of references to which stops 
# they like
class BusStop(models.Model):
    stop_id = models.CharField(blank=True, max_length=30)
    name = models.CharField(blank=True, max_length=200)
    default = models.BooleanField(default=False)
    owner = models.ForeignKey(Profile)

    def __str__(self):
      return str(self.name + "(" + self.stop_id + ")") 
