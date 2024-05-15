from django.db import models
from PIL import Image, ImageDraw, ImageFont
import os

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    username = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)

    @staticmethod
    def generate_profile_image(username, gender):
        os.makedirs('media/profile_images', exist_ok=True)
        filename = f"profile_images/{username}.png"
        image = Image.new('RGB', (200, 200), color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        color = 'blue' if gender.lower() == 'male' else 'pink'
        draw.text((50, 50), username, fill=color, font=font)
        image.save(f"media/{filename}")
        return filename

    @classmethod
    def create(cls, username, gender, email, location):
        profile_image = cls.generate_profile_image(username, gender)
        return cls.objects.create(
            username=username,
            gender=gender,
            email=email,
            location=location,
            profile_image=profile_image
        )

    @classmethod
    def search_users(cls, name, email, location):
        return cls.objects.filter(
            username__icontains=name,
            email__icontains=email,
            location__icontains=location
        )

    def __str__(self):
        return self.username
