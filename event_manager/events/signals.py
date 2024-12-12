from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Registration  # Используем модель Registration

@receiver(post_save, sender=Registration)
def send_registration_email(sender, instance, created, **kwargs):
    if created:

        event = instance.event
        user = instance.user
        subject = f"Registration Confirmed for {event.title}"
        message = f"Hello {user.username},\n\nYou have successfully registered for the event: {event.title}.\nEvent Details:\nLocation: {event.location}\nStart Time: {event.date}\n\nBest regards,\nYour Event Team."
        recipient = user.email

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
