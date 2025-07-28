from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from core.models import Stock


@receiver(post_save, sender=Stock)
def stock_alert_email(sender, instance, created, **kwargs):
    if instance.a_commande > 0:
        send_mail(
            subject = f"Stock alert: {instance.article.name}",
            message = f"... alert text ...",
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [settings.DEFAULT_FROM_EMAIL, 'yosra.kachroud@hutchinson.com'],
            fail_silently=False,
        )
