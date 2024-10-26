from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    is_2fa_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # This indicates a new instance
            print("Attempting to create a new Profile instance for user:", self.user)
        else:
            print("Updating Profile instance for user:", self.user)
        super(Profile, self).save(*args, **kwargs)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('create_user_profile')
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()