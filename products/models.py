from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=150, unique=True)
    description = models.TextField("Описание")
    cost = models.DecimalField("Стоимость", max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

    def __str__(self):
        return self.name
