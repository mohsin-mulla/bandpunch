from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from datetime import datetime

from ticket.models import Venue, Event, Artist, Genre, Purchase
from ticket.forms import PurchaseForm, UserForm, UserProfileForm

from carton.cart import Cart

# Create your views here.
def index(request):
    return render(request, 'ticket/staticpages/index.html')

def browse_artists(request):
    # Obtain the context from the HTTP request
    artists_list = Artist.objects.order_by('name')

    # Create a dictionary to pass the list into the template engine.
    context_dict = {'artists': artists_list}

    # Render the response into the template file
    return render(request, 'ticket/browse/artists.html', context_dict)

def browse_events(request):
    events_list = Event.objects.order_by('date')

    context_dict = {'events': events_list}

    return render(request, 'ticket/browse/events.html', context_dict)

def event_view(request, event_name_url):
    # Try used for exception handling
    try:
        # Query filtering all product objects from the category name
        event = Event.objects.filter(slug__iexact=event_name_url)
        
        context_dict = {'event': event[0]}
        
    except Event.DoesNotExist:
        pass

    return render(request, 'ticket/browse/event_view.html', context_dict)

def browse_venues(request):
    venues_list = Venue.objects.order_by('name')

    context_dict = {'venues': venues_list}

    return render(request, 'ticket/browse/venues.html', context_dict)

def about(request):
    return render(request, 'ticket/staticpages/about.html')

def terms(request):
    return render(request, 'ticket/staticpages/terms.html')

def add(request):
    cart = Cart(request.session)
    event = Event.objects.get(id=request.GET.get('id'))
    cart.add(event, price=event.price)

    messages.success(request, "Event added to basket")

    return render(request, 'ticket/cart/basket.html')

def remove(request):
    cart = Cart(request.session)
    event = Event.objects.get(id=request.GET.get('id'))
    cart.remove_single(event)

    messages.success(request, "Event removed from basket")

    return render(request, 'ticket/cart/basket.html')

def show_cart(request):
    cart = Cart(request.session)
    total = cart.total

    return render(request, 'ticket/cart/basket.html', {'total': total})

def checkout(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)

        session = request.session.session_key  # grab session key for identifying correct record
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") # add submit time to ensure validity
        session_id = session + " " + now

        if form.is_valid():
            valid_form = form.save(commit=False) # don't save yet till session key is stored

            valid_form.temp_session_key = session_id # assign session key to temp_session_key field
            valid_form.save() # save entry

            data = form.cleaned_data
            recipient = data['email']

            ref_filter = Purchase.objects.filter(temp_session_key__iexact=session_id).values_list('reference_number')

            if len(recipient) > 0:
                context_dict = {'ref_number': ref_filter, 'details': data}

                messages.success(request, "Receipt sent successfully!")

                subject = "Your Booking Reference: "
                to = [recipient]
                from_email = 'orders@bandpunch.net'

                template = get_template('ticket/email/booking_reference.html')
                context = RequestContext(request, locals())
                template = template.render(context)

                message = EmailMultiAlternatives(subject, template, from_email, ['emailaddress@goeshere.com'])
                message.attach_alternative(template, "text/html")
                message.send(True)

                return render(request, 'ticket/cart/booking_reference.html', context_dict)     
            else:
                context_dict = {'ref_number': ref_filter, 'details': data}

                return render(request, 'ticket/cart/booking_reference.html', context_dict)     
        else:
            print (form.errors)
    else:
        form = PurchaseForm()
    return render(request, 'ticket/cart/checkout.html', {'form': form})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/registration_form.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})