import warnings
import random

from faker import Factory
from fabric.api import local
from fabric.contrib import django
from fabric.colors import green

django.project('bokamerki')
from django.contrib.auth.models import User
from apps.lists.models import List
from apps.clips.models import Clip
from apps.comments.models import Comment


def setup():
    print green('Running syncdb...')
    local('./manage.py syncdb')

    print green('Running migrate...')
    local('./manage.py migrate')

def bootstrap():
    print green('Hang tight! Bootstrapping...')
    fake = Factory.create()
    user = User.objects.get(pk=1)
    list_titles = ['Design', 'Python', 'Git', 'Startups', 'Django', 'Ember.js']

    _list = List.objects.create(
        title='Inbox',
        user=user,
        description=fake.sentence()
    )

    clip = Clip.objects.create(
        title='Blimp',
        url='http://getblimp.com',
        user=user,
        list=_list,
        notes=fake.text(),
        favicon_url='https://plus.google.com/_/favicon?domain=getblimp.com'
    )

    clip.likes.add(user)

    comment = Comment.objects.create(
        body=fake.text(),
        user=user
    )

    clip.comments.add(comment)

    print green('Creating users...')

    users = []
    for i in range(0, 3):
        users.append(User(
            email=fake.email(),
            username=fake.userName(),
            first_name=fake.firstName(),
            last_name=fake.lastName()
        ))

    User.objects.bulk_create(users)

    print green('Creating lists...')
    lists = []

    for i in range(1, 4):
        lists.append(List(
            title=random.choice(list_titles),
            user=User.objects.get(pk=i+1),
            description=fake.sentence()
        ))

    List.objects.bulk_create(lists)

    print green('Creating clips, likes, and comments...')

    for i in range(0, 100):
        users = []
        comments = []

        clip = Clip.objects.create(
            url=fake.url(),
            user=User.objects.order_by('?')[0],
            list=_list,
            notes=fake.text()
        )

        for i in range(0, 4):
            users.append(User.objects.get(pk=i+1))

        clip.likes.add(*users)

        for i in range(0, 15):
            comments.append(Comment.objects.create(
                body=fake.text(),
                user=User.objects.order_by('?')[0]
            ))

        clip.comments.add(*comments)


warnings.filterwarnings("ignore", category=DeprecationWarning)
