from django.db import models
from products.models import Product


class Contract(models.Model):
    name = models.CharField("Название", max_length=150, unique=True)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="contracts", verbose_name="Услуга"
    )
    document = models.FileField("Файл договора", upload_to="contracts/", blank=True)
    start_date = models.DateField("Дата заключения")
    end_date = models.DateField("Дата окончания")
    cost = models.DecimalField("Сумма", max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "контракт"
        verbose_name_plural = "контракты"
        ordering = ("-start_date",)

    def __str__(self):
        return self.name
