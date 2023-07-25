# certificates/models.py
from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='certificates/pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title

