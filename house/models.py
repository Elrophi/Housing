from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class NeighbourHood(models.Model):
    name = models.CharField()
    location = models.CharField()
    count = models.IntegerField()
    admin =models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="my_hood")

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, n_id):
        return cls.objects.filter(id=n_id)

class Profile(models.Model):
    name = models.CharField()
    profile_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, blank=True, related_name="members")
    email = models.EmailField()

    def __str__(self):
        return self.name

    @receiver(post_save, sender=User)   
    def create_user_profile(sender, instance,  created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def _save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    name = models.CharField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="owner")
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name="business")
    email = models.EmailField()

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()
        
    