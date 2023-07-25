

# certificates/views.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
# certificates/views.py
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, get_object_or_404


from .models import Certificate

def create_certificate(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        certificate = Certificate.objects.create(title=title, content=content)

        # Generate the PDF certificate
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.drawString(100, 750, "Certificate ID: {}".format(certificate.id))
        c.drawString(100, 700, "Title: {}".format(certificate.title))
        c.drawString(100, 650, "Content: {}".format(certificate.content))
        c.save()

        buffer.seek(0)

        # Save the PDF to the model's pdf_file field
        certificate.pdf_file.save('certificate_{}.pdf'.format(certificate.id), buffer)

        return render(request, 'certificates/certificate_created.html', {'certificate': certificate})

    return render(request, 'certificates/create_certificate.html')








def verify_certificate(request):
    if request.method == 'POST':
        certificate_id = request.POST['certificate_id']
        certificate = get_object_or_404(Certificate, id=certificate_id)

        # Generate the PDF certificate for verification
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.drawString(100, 750, "Certificate ID: {}".format(certificate.id))
        c.drawString(100, 700, "Title: {}".format(certificate.title))
        c.drawString(100, 650, "Content: {}".format(certificate.content))
        c.save()

        buffer.seek(0)

        # Prepare the response with PDF data
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="certificate_{}.pdf"'.format(certificate.id)
        return response

    return render(request, 'certificates/verify_certificate.html')







