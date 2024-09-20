"""
Signal handlers for the MainApp Django application.

This module defines signals that are triggered during specific model events, such as saving an Order.
It includes functionality for generating unique slugs for Order instances before they are saved.

- create_slug: A helper function that generates a unique slug based on a specified field and checks for existing slugs.
- presave_order: A signal handler that sets a unique slug for Order instances before saving them to the database.
"""


from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Order


def create_slug(instance, model_class, field_name='item', slug_field='slug', new_slug=None):
    """
    Generate a unique slug for the given model instance.

    Args:
        instance: The model instance to generate a slug for.
        model_class: The model class to check for existing slugs.
        field_name: The name of the field to base the slug on (default is 'item').
        slug_field: The name of the field to store the slug (default is 'slug').
        new_slug: A new slug to use if provided.

    Returns:
        A unique slug string.
    """
    slug = slugify(getattr(instance, field_name))  # Create slug from the 'item' field
    if new_slug is not None:
        slug = new_slug
    model_class_qs = model_class.objects.filter(**{slug_field: slug})  # Check if slug exists
    if model_class_qs.exists():
        new_slug = f"{slug}-{model_class_qs.first().id}"  # Append ID to slug if it already exists
        return create_slug(instance, model_class, field_name, slug_field, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Order)
def presave_order(sender, instance, *args, **kwargs):  # pylint: disable=W0613
    """
    Signal handler to set a unique slug for Order instances before saving.
    """
    if not instance.slug:  # Only set the slug if it doesn't exist
        instance.slug = create_slug(instance, Order)  # Generate and set the unique slug
