from import_export import resources
from .models import *

class predone(resources.ModelResource):
    class Meta:
        model = pred_one

class prodarea(resources.ModelResource):
    class Meta:
        model = prod_area

class one(resources.ModelResource):
    class Meta:
        model = one

class two(resources.ModelResource):
    class Meta:
        model = two

class three(resources.ModelResource):
    class Meta:
        model = three
class pred_three(resources.ModelResource):
    class Meta:
        model = pred_three