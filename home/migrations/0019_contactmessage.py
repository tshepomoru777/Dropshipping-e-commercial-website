class ContactMessage(models.Model):
    name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=False, max_length=50)  # Now using EmailField
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=500)  # Increased message length
    ip = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=50)  # Consider renaming for clarity
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['created_at']),
        ]
