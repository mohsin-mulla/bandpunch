from django.db import models
from django.db import transaction
from django.db.models import F
from django.core.validators import RegexValidator, validate_email
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import datetime

from random import randrange

from ticket.fields import CreditCardField, ExpiryDateField, VerificationValueField

# Regular Expressions used by models
alphanumeric_RE = RegexValidator(r'^[A-Za-z0-9\s]*$', 'Only alphanumeric characters are allowed.')

# CONSTANTS
# Unique reference generator, many thanks to github user workmajj, using Crockford's Encoding
CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LENGTH = 16
MAX_TRIES = 1024

# MODELS
class Genre(models.Model):
    genre = models.CharField(max_length=30, default=None, unique=True)

    def __str__(self):
        return self.genre

    class Meta:
        ordering = [ "genre" ]
        verbose_name_plural = "genres"

class CardChoices(models.Model):
    """ Used by the purchase form. """
    payment_type = models.CharField(max_length=30, default=None, unique=True)

    def __str__(self):
        return self.payment_type

    class Meta:
        ordering = [ "payment_type" ]
        verbose_name_plural = "payment types"

class Venue(models.Model):
    """The 'Venue' model represents a collection of different venues."""
    name = models.CharField(max_length=30, default=None)
    address = models.CharField(max_length=255, default=None)
    capacity = models.PositiveIntegerField(default=0)
    website = models.URLField(max_length=50, null=True)
    phone_number = models.CharField(validators=[
        RegexValidator(regex='^\d{11}$', message='Length has to be 11',
            code='Invalid number')], blank=True, null=True, max_length=11)
    description = models.TextField()
    image = models.ImageField(upload_to='venue/images')
    slug = models.SlugField(unique=True, default=None)

    # Returns the name of a category
    def __str__(self):
        return self.name

    # Call the slugify method and update the slug field when the name is changed
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Venue, self).save(*args, **kwargs)

    class Meta:
        # Orders the categories using the name field in ascending order
        ordering = [ "name" ]
        verbose_name_plural = "venues"    

class Artist(models.Model):
    """The 'Artist' model represents a collection of different artists."""
    name = models.CharField(max_length=30, default=None)
    description = models.TextField()
    image = models.ImageField(upload_to='artist/images')
    genre = models.ForeignKey('Genre', related_name='genres', default=None)
    slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        ordering = [ "name" ]
        verbose_name_plural = "artists"

class Event(models.Model):
    """The 'Event' model represents a collection of different events."""
    artists = models.ManyToManyField(Artist) # Many artists can play at one event
    venue = models.ForeignKey(Venue)
    name = models.CharField(max_length=255, default=None)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='event/images')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    curfew_time = models.TimeField(blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, default=None)

    class Meta:
        ordering = [ "name" ]
        verbose_name_plural = "events"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    # Calculate the number of tickets remaining
    def get_tickets(event_id, num_tickets):
        with transaction.atomic():
            Event.objects.filter(id=event_id).update(quantity=F('quantity') - num_tickets)
            if Event.objects.get(id=venue_id).quantity < 0:
                raise ValueError("Capacity exceeded: less than %s tickets left." % num_tickets)

class UserAccount(models.Model): # needs to be associated with INDIVIDUAL purchases, a user can hold more than one purchase
    user = models.OneToOneField(User) # Links user account with a Django User model instance
    #event = models.ForeignKey(Event, blank=True)
    name = models.CharField(max_length=30)    
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=11, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 11', code='Invalid number')])
    email = models.EmailField(validators=[validate_email])

    def __str__(self):
        return self.user.email

class Purchase(models.Model): # needs to be associated with a user account
    cash_only = models.BooleanField('Cash only', default=False)
    payment_type = models.ForeignKey('CardChoices', related_name='Payment Types')
    card_name = models.CharField(max_length=26, default=None, validators=[alphanumeric_RE])
    card_number = models.CharField(max_length=19, default=None) # OVERWRITTEN
    security_code = models.IntegerField(max_length=3, default=None) # OVERWRITTEN
    expiry_date = models.DateField(default=datetime.now) # OVERWRITTEN
    date = models.DateField(editable=True, auto_now_add=True, default=datetime.now)
    delivery_option = models.BooleanField('Is Collecting Ticket', default=True)
    reference_number = models.CharField(max_length=LENGTH, unique=True, default=None)
    temp_session_key = models.CharField(null=True, editable=False, max_length=255, default=None) # Used for identification of unique record

    def __str__(self):
        return self.card_name

    def save(self, *args, **kwargs): # Thanks to workmajj for providing the logic!
        """
        Upon saving, generate a code by randomly picking LENGTH number of
        characters from CHARSET and concatenating them. If code has already
        been used, repeat until a unique code is found, or fail after trying
        MAX_TRIES number of times. (This will work reliably for even modest
        values of LENGTH and MAX_TRIES, but do check for the exception.)
        Discussion of method: http://stackoverflow.com/questions/2076838/
        """
        loop_num = 0
        unique = False
        while not unique:
            if loop_num < MAX_TRIES:
                new_code = ''
                for i in range(LENGTH):
                    new_code += CHARSET[randrange(0, len(CHARSET))]
                if not Purchase.objects.filter(reference_number=new_code):
                    self.reference_number = new_code
                    unique = True
                loop_num += 1
            else:
                raise ValueError("Couldn't generate a unique code.")
        super(Purchase, self).save(*args, **kwargs)

    class Meta:
        ordering = [ "date" ]