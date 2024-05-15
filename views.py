from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import io
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse

def search_users(request):
    name = request.GET.get('name', None)
    email = request.GET.get('email', None)
    location = request.GET.get('location', None)
    
    users = User.objects.all()
    if name:
        users = users.filter(username__icontains=name)
    if email:
        users = users.filter(email__icontains=email)
    if location:
        users = users.filter(profile__location__icontains=location)
    
    data = [{'username': user.username, 'email': user.email, 'location': user.profile.location} for user in users]
    return JsonResponse(data, safe=False)


def generate_profile_image(request, username, gender):
    width, height = 200, 200
    background_color = "white"
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    initials = username[0].upper()
    font = ImageFont.truetype("arial.ttf", 80)
    text_color = "black"
    text_width, text_height = draw.textsize(initials, font=font)
    draw.text(((width - text_width) // 2, (height - text_height) // 2), initials, fill=text_color, font=font)
    byte_io = io.BytesIO()
    image.save(byte_io, "PNG")
    return HttpResponse(byte_io.getvalue(), content_type="image/png")

