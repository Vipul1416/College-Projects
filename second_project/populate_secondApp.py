import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django 
django.setup()

import random
from secondApp.models import Topic,AccessRecord,Webpage
from faker import Faker 

fakegen=Faker()
topics=['Social','Games','sn','MArketPlace','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(M=5):
    for entry in range(M):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(30)
    print("Populated")


