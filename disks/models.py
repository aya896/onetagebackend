from django.db import models


class Disk(models.Model):

    MODEL_CHOICES = [
        ("octa", "Octa Wood"),
        ("circle", "Cercle Tag"),
        ("capsule", "Capsule Soft"),
    ]

    MATERIAL_CHOICES = [
        ("light_wood", "Bois texture claire"),
        ("dark_wood", "Bois sombre"),
        ("black_wood", "Bois noire"),
        ("white_pvc", "PVC blanc"),
        ("black_pvc", "PVC noir"),
    ]

    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to="disks/")

    def __str__(self):
        return f"{self.get_model_display()} - {self.get_material_display()}"