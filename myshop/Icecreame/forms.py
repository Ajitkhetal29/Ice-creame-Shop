from django import forms
from .models import Item , Item1 , Order , Order1

# Item form for Icecreame 
class ItemForm(forms.ModelForm):
    class Meta :
        model = Item
        fields = ['prod_code','item_name', 'item_desc', 'item_price', 'item_image']


# Item form for Softy
class Item1Form(forms.ModelForm):
    class Meta :
        model = Item1
        fields = ['prod1_code','item1_name', 'item1_desc', 'item1_price', 'item1_image']

class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id' ,'quantity' ,'user']  
class UpdateOrderForm1(forms.ModelForm):
    class Meta :
        model = Order1
        fields = ['order1_id' , 'quantity' , 'user']