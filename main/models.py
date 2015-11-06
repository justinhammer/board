from django.db import models
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password, first_name, last_name, is_staff, is_superuser, is_active=True, **extra_fields):
        now = timezone.now()

        # if username != None:
        #     email = username

        # if not email:
        #     raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                            is_staff=is_staff,
                            is_active=True,
                            is_superuser=is_superuser,
                            last_login=now,
                            date_joined=now,
                            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name=None, last_name=None, username=None, password=None, email=None, **extra_fields):
        return self._create_user(email, username, password, first_name, last_name, False, False, **extra_fields)

    def create_superuser(self, username=None, password=None, email=None, **extra_fields):
        return self._create_user(email, username, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    user_bio = models.TextField(null=True, blank=True)
    email = models.EmailField('email address', max_length=255, unique=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    profile_pic = models.ImageField(upload_to="profile_pics", null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Thread(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)


class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser, blank=True, null=True)
    thread = models.ForeignKey(Thread, blank=True, null=True)
    body = models.TextField(null=True, blank=True)
    upvotes = models.ManyToManyField('main.CustomUser', related_name='up_votes')
    downvotes = models.ManyToManyField('main.CustomUser', related_name='down_votes')
    
    def total_votes(self):
        total_votes = len(self.upvotes) - len(self.downvotes)
        return total_votes

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

    
