import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "products.settings") # Tên app bạn tạo ( QUAN TRỌNG ).
django.setup()
from products.models import Data # Import Model đã tạo 

class DataObject():

    def __init__(self):
        pass

    def create(self, name, link, price, description):
        # Ta sẽ insert data bằng phương thức create
        return Data.objects.create(name=name, link = link , price = price, description = description)