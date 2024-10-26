from django.conf import settings
from django.db import models
import mptt.models
from django.core.validators import MinValueValidator, MaxValueValidator


class Comment(mptt.models.MPTTModel):
    subject = models.CharField(blank=True, max_length=50)
    comment = models.TextField(blank=True)  # TextField with no max_length limit for flexibility
    rate = models.IntegerField(
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Ensures the rating is between 1 and 5
    )
    ip = models.CharField(blank=True, max_length=20)  # Stores the IP address of the user
    create_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the comment is created
    update_at = models.DateTimeField(auto_now=True)  # Automatically updated when the comment is modified

    # MPTT-related fields to manage hierarchical (nested) comments
    parent = mptt.fields.TreeForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, related_name='replies'
    )

    # ForeignKey linking the comment to the associated product
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')

    # ForeignKey linking the comment to the user who created it
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # MPTTMeta allows you to configure options like ordering for MPTT models
    class MPTTMeta:
        order_insertion_by = ['create_at']  # Order comments within the tree by creation time

    # Optional Meta class to specify default ordering of comments by creation time
    class Meta:
        ordering = ['create_at']  # Default ordering of comments (oldest first)