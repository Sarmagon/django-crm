from django.db import models
from products.models import Product


class Advertisement(models.Model):
    name = models.CharField("Название", max_length=150, unique=True)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="advertisements", verbose_name="Услуга"
    )
    channel = models.CharField("Канал продвижения", max_length=150)
    budget = models.DecimalField("Бюджет на рекламу", max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "рекламная кампания"
        verbose_name_plural = "рекламные кампании"

    def __str__(self):
        return self.name
