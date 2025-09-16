from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Place(models.Model):
    PLACE_TYPES = [
        ('cafe', 'Кафе'),
        ('park', 'Парк'),
        ('cinema', 'Кінотеатр'),
        ('other', 'Інше'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    place_type = models.CharField(max_length=20, choices=PLACE_TYPES)
    location = models.CharField(max_length=200, blank=True, null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='places/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def preview_description(self):
        return ' '.join(self.description.split()[:10]) + '...' if len(
            self.description.split()) > 10 else self.description

    def get_star_rating(self):
        return '★' * self.rating + '☆' * (5 - self.rating)

    def get_place_type_display(self):
        return dict(self.PLACE_TYPES).get(self.place_type, self.place_type)

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/image/default.jpg'