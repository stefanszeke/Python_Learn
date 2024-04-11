# 1 install django
pip install django

# 2 create project
django-admin startproject name_project

# 3 run server
python manage.py runserver

# 4 create app
python manage.py startapp name_app

# 5 views.py -> urls.py -> settings
create urls.py in app
link apps views.py to urls.py 
link apps urls.py to project urls.py

# migration
python manage.py migrate
- create database
python manage.py makemigrations
- create migration file, meaning create table

# 6 create model
add data with python shell
python manage.py shell
import model from app.models\
from app.models import Model
Item.objects.all() # show all data
Item.objects.create(item_name='name', item_desc='desc', item_price=100) # add data
food1 = Item()
food1.item_name = 'name'
food1.item_desc = 'desc'
food1.item_price = 100
food1.save()

# 7 create super user
python manage.py createsuperuser
add model to admin.py
from .models import Item
