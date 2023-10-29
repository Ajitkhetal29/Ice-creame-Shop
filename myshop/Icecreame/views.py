from django.shortcuts import render , redirect
from django.http import HttpResponse
from datetime import date, datetime
from Icecreame.models import Item , Item1 , History  ,WishlistItem , WishlistItem1 ,Order , Order1
from Icecreame.models import Contact 
from django.template import loader
from Icecreame.forms import ItemForm , Item1Form , UpdateOrderForm , UpdateOrderForm1
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum




#  Main Page View  
def index(request):
    item_list = Item.objects.all()
    item1_list = Item1.objects.all()
    item_list = item_list[:3] 
    item1_list = item1_list[:3]
    context ={
        "item_list":item_list,
        "item1_list":item1_list
    }
    return render(request, 'icecreame/index.html',context)


# Icecreame Type Items page view
def icecreame(request):
    item_list = Item.objects.all()
    context ={
        "item_list":item_list
    }
    return render(request, 'icecreame/icecreame.html',context)


# Softy Type Items page view
def softy(request):
    # return HttpResponse ("Hello World this index page")
    item_list = Item1.objects.all()
    context ={
        "item_list":item_list
    }
    return render(request, 'icecreame/softy.html',context)


# Detail view for Icecreams
@login_required
def detail(request , item_id):
    item = Item.objects.get(pk=item_id)
    hist = History.objects.filter(prod_ref = item.prod_code).order_by('-event_datetime')[:3]

    context = {
        "item":item,
        'hist':hist,
    }
    return render (request ,'icecreame/detail.html',context)


# Detail view for softys 
@login_required
def detail1(request , item1_id):
    item1 = Item1.objects.get(pk=item1_id)
    hist = History.objects.filter(prod_ref = item1.prod1_code).order_by('-event_datetime')[:3]
  

    context = {
        "item1":item1,
        'hist':hist,
        

    }
    return render (request, 'icecreame/detail1.html',context)


# Icecreame Item Add view
@login_required
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        obj_History = History(
            item_name = request.POST['item_name'],
            prod_ref = form.instance.prod_code,
            op_type = 'Created'
        )
        obj_History.save()
        form.save()
        
        messages.success(request, "Thank You ! .. Item Added Succesfully")

        return redirect ('Icecreame:detail')
    return render(request ,'icecreame/item-form.html',{'form':form})


# Softy Item add View
@login_required
def create_item1(request):
    form = Item1Form(request.POST or None)

    if form.is_valid():
        form.save()
       
        messages.success(request, "Thank You ! .. Item Added Succesfully")
        return redirect ('Icecreame:detail')
    return render(request ,'icecreame/item1-form.html',{'form':form})


# Contact view 
@login_required
def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')


        contact = Contact(name=name , email=email, phone=phone, msg=msg, date= datetime.today())
        contact.save()
        messages.success(request, "Thank You ! ..Your response has been submitted")
        return redirect("Icecreame:review")
    return render (request , "icecreame/contact.html")


# Review view
def review(request):
    review_list = Contact.objects.all()
    context = {
        "review_list":review_list
    }

    return render(request,"icecreame/review.html",context)


# Update Icecrea,e view
@login_required
def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        obj_History = History(
            item_name = request.POST['item_name'],
            prod_ref = item.prod_code,
            op_type = 'Updated'
        )
        obj_History.save()
        messages.success(request, "Thank You ! .. Item Updated Succesfully")
        return redirect ('Icecreame:detail' , item_id =id)
    return render(request, 'icecreame/item-update.html', {'form':form, 'item':item})


# update softy view
@login_required
def update_item1(request,id):
    item = Item1.objects.get(id=id)
    form = Item1Form(request.POST or None , instance =item)

    if form.is_valid():
        form.save()
        obj_History = History(
            item_name = request.POST['item1_name'],
            prod_ref = item.prod1_code,
            op_type = 'Updated'
        )
        obj_History.save()
        messages.success(request, "Thank You ! .. Item Updated Succesfully")
        return redirect ('Icecreame:detail1' , item1_id =id )
    return render(request, 'icecreame/item1-update.html', {'form':form, 'item':item})


# Delete Icecreame View
@login_required
def delete_item(request, id):
    item=Item.objects.get(id=id)
    
    context= {
        'item':item ,
    }

    if request.method=="POST":
        obj_History = History(
            item_name = item.item_name,
            prod_ref = item.prod_code,
            op_type = 'Deleted'
        )
        obj_History.save()
        item.delete()
        
        messages.success(request, "Thank You ! .. Item Deleted Succesfully")
        return redirect('Icecreame:icecreame')

    return render(request, 'icecreame/item-delete.html',context)



# Delete softy view
@login_required
def delete_item1(request , id):
    item = Item1.objects.get(id=id)

    context = {
        'item':item
    }
    if request.method=="POST":
        item.delete()
        obj_History = History(
            item_name = item.item1_name,
            prod_ref = item.prod1_code,
            op_type = 'Deleted'
        )
        obj_History.save()
        messages.success(request, "Thank You ! .. Item Deleted Succesfully")
        return redirect('Icecreame:softy')
    return render(request, 'icecreame/item-delete1.html',context)


# wishlist view
@login_required
def add_to_wishlist(request,item_id):
    if request.user.is_authenticated:
        item = Item.objects.get(pk=item_id)
        WishlistItem.objects.get_or_create(user = request.user , item=item)
        return redirect('Icecreame:view_wishlist')
    return render('Icecreame:detail' , item_id=item_id)

# remove from wisjlist
@login_required
def remove_from_wishlist(request,item_id):
    if request.user.is_authenticated:
        item = Item.objects.get(pk=item_id)
        wishlistitem = WishlistItem.objects.get(user = request.user , item=item)
        wishlistitem.delete()
        return redirect('Icecreame:view_wishlist')
    return render('Icecreame:detail' , item_id=item_id)

# add from wisjlist
@login_required
def add_to_wishlist1(request,item1_id):
    if request.user.is_authenticated:
        item1 = Item1.objects.get(pk=item1_id)
        WishlistItem1.objects.get_or_create(user = request.user , item1=item1)
        return redirect('Icecreame:view_wishlist')
    return render('Icecreame:detail' , item1id=item1_id)

# remove from wisjlist
@login_required
def remove_from_wishlist1(request,item1_id):
    if request.user.is_authenticated:
        item1 = Item1.objects.get(pk=item1_id)
        wishlistitem = WishlistItem1.objects.get(user = request.user , item1=item1)
        wishlistitem.delete()
        return redirect('Icecreame:view_wishlist')
    return render('Icecreame:detail' , item1_id=item1_id)

# vvishlist
@login_required    
def view_wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user)
        wishlist_items1 = WishlistItem1.objects.filter(user=request.user)
        context = {
            'wishlist_items': wishlist_items,
            'wishlist_items1': wishlist_items1
        }
        return render(request, 'icecreame/wishlist.html',context)
    return render(request, 'icecreame/wishlist.html', {'wishlist_items': []})

# order view
@login_required
def cust_order(request,item_id):
    if request.user.is_authenticated:
        item = Item.objects.get(pk=item_id)
        Order.objects.get_or_create(user = request.user,item=item)
        return redirect('Icecreame:order_list')
    return render('Icecreame:detail' , item_id=item_id)

# order view
@login_required
def cust_order1(request,item1_id):
    if request.user.is_authenticated:
        item1 = Item1.objects.get(pk=item1_id)
        Order1.objects.get_or_create(user = request.user,item1=item1)
        return redirect('Icecreame:order_list')
    return render('Icecreame:detail' , item1_id=item1_id)


# order list
def order_list(request):
    if request.user.profile.user_type == 'Rest' or request.user.profile.user_type == 'Admin':
        order_list = Order.objects.all()
        order_list1 = Order1.objects.all()
        total_price = 0
        total_price1 = 0

        for o in order_list:
            total_price += (o.item.item_price * o.quantity)
            o.total_price = total_price

        for o in order_list1:
            total_price1 += (o.item1.item1_price * o.quantity)
            o.total_price1 = total_price1



        context = {
                'order_list': order_list,
                'order_list1': order_list1,  
                'total_price':  total_price,
                'total_price1': total_price1   
               
        }
    
    elif request.user.profile.user_type == 'Cust':
        order_list = Order.objects.filter(user=request.user)
        order_list1 = Order1.objects.filter(user=request.user)
        total_price = 0
        total_price1 = 0

        for o in order_list:
            total_price += (o.item.item_price * o.quantity)
            o.total_price = total_price

        for o in order_list1:
            total_price1 += (o.item1.item1_price * o.quantity)
            o.total_price1 = total_price1

        context = {
                'order_list': order_list,
                'order_list1': order_list1,
                'total_price':  total_price,
                'total_price1': total_price1  
        }
        return render(request, 'icecreame/order-list.html',context)
    return render(request, 'icecreame/order-list.html',context)
    
def total_price(self):
        return self.price_per_unit * self.individual_quantity

# update order view
def update_order(request , item_id , upd_order_id):
    OrdeItem = Order.objects.get(order_id=upd_order_id)
    form = UpdateOrderForm(request.POST or None , instance = OrdeItem)

    context = {
        'item_id':item_id,
        'upd_order_id':upd_order_id,
        'form':form,
    }
    if form.is_valid():
        OrdeItem.save()
        form.save()
       
        return redirect('Icecreame:order_list')
    return render(request , 'icecreame/orders_upd.html',context)

# update order view
def update_order1(request , item1_id , upd_order1_id):
    OrdeItem1 = Order1.objects.get(order1_id=upd_order1_id)
    form = UpdateOrderForm1(request.POST or None , instance = OrdeItem1)
    context = {
        'item1_id':item1_id,
        'upd_order1_id':upd_order1_id,
        'form':form,
    }
    if form.is_valid():
        OrdeItem1.save()
        form.save()
       
        return redirect('Icecreame:order_list')
    return render(request , 'icecreame/orders_upd1.html',context)


