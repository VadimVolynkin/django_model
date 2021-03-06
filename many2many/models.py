from django.db import models






# class Group(models.Model):
#     name = models.CharField(max_length=128)
#
#
#     def __str__(self):
#         return self.name

# class Person(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership', through_fields=('group', 'person'),)
#
#     def __str__(self):
#         return self.name
#
# class Membership(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     inviter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="membership_invites",)
#     invite_reason = models.CharField(max_length=64)
#
#     def __str__(self):
#         return f'{self.person}({self.group}), invite by {self.inviter} - {self.invite_reason}'


################## symmetrical=False
from django.urls import reverse


class Subscribers(models.Model):
    """if you are my subscriber, I`am your subscriber too"""
    name = models.CharField(max_length=50)
    subscribers = models.ManyToManyField("self", symmetrical=True, related_name='some', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subscriber_detail', kwargs={'id': self.pk})







# class Friends(models.Model):
#     """if you are my friend, I`am your friend too"""
#     name = models.CharField(max_length=50)
#     friends = models.ManyToManyField('self', blank=True)
#
#     def __str__(self):
#         return self.name
