from django.shortcuts import render,redirect
from store_app.models import Product,Categories,Filter_Price,Color,Brand,Contact,Order,OrderItem
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt
import razorpay 

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRECT))
#from .models import Profile
def BASE(request):
	return render(request,'Main/base.html')

def HOME(request):
	product = Product.objects.filter(status = 'Publish')

	context = {
		'product':product,
	}
	return render(request,'Main/index.html',context)


def PRODUCT(request):
	categories = Categories.objects.all() 
	filter_price = Filter_Price.objects.all()
	color = Color.objects.all()
	brand = Brand.objects.all()

	CATID = request.GET.get('categories')
	FILTER_PRICE_ID = request.GET.get('filter_price')
	print(FILTER_PRICE_ID)
	COLID = request.GET.get('color')
	BRID = request.GET.get('brand')
	ATOZID = request.GET.get('ATOZ')
	print(ATOZID)
	ZTOAID = request.GET.get('ZTOA')
	print(ZTOAID)
	LOWID = request.GET.get('low_to_heigh')
	print(LOWID)
	HIGHID = request.GET.get('heigh_to_low')
	print(HIGHID)
	
	if CATID:
		product = Product.objects.filter(categories = CATID,status= "Publish")
	elif FILTER_PRICE_ID:
		product = Product.objects.filter(Filter_Price = FILTER_PRICE_ID,status= "Publish")
	elif COLID:
		product = Product.objects.filter(color = COLID,status= "Publish")
	elif BRID:
		product = Product.objects.filter(Brand= BRID,status= "Publish")
	elif ATOZID:
		product = Product.objects.filter(status= "Publish").order_by('-name')				
	elif ZTOAID:
		product = Product.objects.filter(status= "Publish").order_by('name')
	elif LOWID:
		product = Product.objects.filter(status= "Publish").order_by('price')
	elif HIGHID:
		product = Product.objects.filter(status= "Publish").order_by('-price')
	

	else:
		product = Product.objects.filter(status = 'Publish')
	
	context = {
		'product':product,
		'categories':categories,
		'filter_price':filter_price,
		'color':color,	
		'brand':brand,
	}

	return render(request,'Main/product.html',context)

def SEARCH(request):
	query = request.GET.get('query')
	product = Product.objects.filter(name__icontains = query)
	context = {
	  'product':product
	 }

	return render(request,'Main/search.html',context)

def SINGLE(request,id):
	prod = Product.objects.filter(id = id).first()
	context = {
	 'prod':prod,
	}
	return render(request,'Main/product_single.html',context)

def Contact_Page(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		contact = Contact(
			name=name,
			email=email,
			subject=subject,
			message=message,
		)

		subject = subject
		message = message
		email_from = settings.EMAIL_HOST_USER
		try:
			send_mail(subject,message,email_from,['angad6382@gmail.com'])
			contact.save()
			return redirect('home')
		except:
			return redirect('contact')



	return render(request,'Main/contact.html')

def REGISTER(request):
	if request.method == "POST":
		username = request.POST.get('username')
		first_name =  request.POST.get('first_name')
		last_name =  request.POST.get('last_name')
		email =  request.POST.get('email')
		pass1 =  request.POST.get('pass1')
		pass2 =  request.POST.get('pass2')

		customer = User.objects.create_user(username,email,pass1)
		customer.first_name = first_name
		customer.last_name =last_name
		customer.save()
		return redirect('register')
	return render(request,'Main/register.html')
	
def LOGIN(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username =username, password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			return redirect('login')

	return render(request,'Main/register.html')

def LOGOUT(request):
	logout(request)

	return redirect('home')

		


@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)

    return redirect("home")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
	return render(request,'Main/cart.html')




def PLACE_ORDER(request):
	if request.method == "POST":
		uid = request.session.get('_auth_user_id')
		user = User.objects.get(id=uid)
		cart = request.session.get('cart')
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		country = request.POST.get('country')
		address = request.POST.get('address')
		city = request.POST.get('city')
		state = request.POST.get('state')
		postcode = request.POST.get('postcode')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		amount = request.POST.get('amount')


		order_id = request.POST.get('order_id')
		payment = request.POST.get('payment')
		context={
			"order_id":order_id
				}

		order=Order(
			user=user,
			firstname=firstname,
			lastname=lastname,
			contry=country,
			address=address,
			city=city,
			state=state,
			postcode=postcode,
			phone=phone,
			email=email,
			payment_id=order_id,
			amount=amount,
		)
		order.save()
		for i in cart:
			a= (int(cart[i]['price']))
			b=(cart[i]['quantity'])
			total=a+b
			item=OrderItem(
				order=order,
				product=cart[i]['name'],
				image=cart[i]['image'],
				quantity=cart[i]['quantity'],
				price=cart[i]['price'],
				total=total,
			)
			item.save()
	return render(request,'Main/place_order.html')


def Checkout(request):
	payment = client.order.create({
		"amount":500,
		"currency":"INR",
		"payment_capture":"1"
	})
	order_id = payment['id']
	context ={
		'order_id':order_id,
		'payment':payment,
	} 
	return render(request,'Main/checkout.html',context)

@csrf_exempt
def SUCCESS(request):
	if request.method == "POST":
		a = request.POST
		order_id = ''
		for key, val in a.items():
			if key == "razorpay_order_id":
				order_id= val
				break


		user = Order.objects.filter(payment_id=order_id).first()
		user.paid = True
		user.save()
	return  render(request,'Main/success.html')