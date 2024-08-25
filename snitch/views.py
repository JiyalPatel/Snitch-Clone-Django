from django.shortcuts import render, redirect
from .models import user, product
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages


# Create your views here.
def index(request):
    allData = product.objects.all()
    trending = []
    other = []
    for data in allData:
        if data.istrend:
            trending.append(data)
        else:
            other.append(data)

    context = {
        'title': 'Home | Snitch',
        'trending': trending,
        'products': other,
    }
    if request.session.get('order_success'):
        context['order_success'] = True
        del request.session['order_success']  # Remove the variable after accessing it

    if request.session.get('order_error'):
        context['order_error'] = True
        del request.session['order_error']  # Remove the variable after accessing it

    return render(request, "index.html", context)


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            userData = user.objects.get(email=email, password=password)

            request.session["login_id"] = userData.id
            request.session.save()
            return redirect(index)
        except:
            return render(request, "login.html", {
                'err': 'Invalid Credentials'
            })
    else:
        return render(request, "login.html", {
            'title': 'Login | Snitch'
        })


def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")

        if user.objects.filter(email=email).exists():
            return render(request, "register.html", {
                'title': 'Register | Snitch',
                'err': 'Email Already Exists'
            })
        else:
            createUser = user(
                name=name, email=email, password=password, address=address, timestamp=""
            )

            createUser.save()

            request.session["login_id"] = user.objects.get(email=email, password=password).id
            request.session.save()
            return redirect(index)
    else:
        return render(request, "register.html", {
            'title': 'Register | Snitch'
        })


def logout(request):
    try:
        del request.session["login_id"]
        return redirect(index)

    except:
        return redirect(login)


def productView(request, id):
    prod = product.objects.get(id=id)
    imgs = [prod.cover, prod.img2, prod.img3, prod.img4, prod.img5]

    allData = product.objects.all()
    trending = []
    for data in allData:
        if data.istrend:
            trending.append(data)

    return render(request, "product.html", {
        'title': 'Product | Snitch',
        'product': prod,
        'imgs': imgs,
        'trending': trending,
    })


def category(request, cat):
    allData = product.objects.all()
    catData = []
    for data in allData:
        if data.category == cat:
            catData.append(data)

    return render(request, "category.html", {
        'title': 'Category | Snitch',
        'cat': cat,
        'data': catData,
    })


def about(request):
    return render(request, "about.html", {
        'title': 'About | Snitch'
    })


def purchase(request, prod):
    if request.session["login_id"]:
        try:
            userData = user.objects.get(id=request.session["login_id"])
            productData = product.objects.get(id=prod)

            message = f"""
            <p>Hi {userData.name},<br>
            Thank you for shopping with <b>Snitch!</b> We're excited to let you know that your order has been received and is being processed.<br><br>
            Order Summary:<br>
            Item: '{productData.name}'<br>
            Amount: ₹{productData.price}<br>
            Shipping Address:<br>
            {userData.address}<br><br>
            Your order will be shipped to you within the next 2-3 business days. Once it's on the way, we'll send you another email.<br><br>
            If you have any questions or need further assistance, feel free to reply to this email or contact our support team at <a href="mailto:support@snitch.com">support@snitch.com</a>.<br><br>
            Thanks again for choosing Snitch. We hope you love your new items!<br><br><br><br><br>
            Best regards,<br>
            The Snitch Team
            </p>
            """

            subject = "Your Snitch Order Confirmation"
            from_email = "project.snitch1@gmail.com"
            recipient = userData.email

            mail = EmailMultiAlternatives(subject, message, from_email, [recipient])
            mail.content_subtype = 'html'  # Setting the email content to HTML
            mail.send()

            request.session['order_success'] = True
            # messages.success(request, 'Your order has been placed successfully, and a confirmation email ha been sent.')

        except:
            request.session['order_error'] = True
            # messages.error(request, 'There was an issue with your order. Please try again.')

        return redirect(index)
    else:
        return redirect(index)
