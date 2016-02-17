@receiver(signals.post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    """It will be called after creation of a new user"""
    if created:
        Employee.objects.get_or_create(
            user=instance, slug=str(instance).replace(' ', '-'))
