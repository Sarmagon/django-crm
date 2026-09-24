from django.core.validators import RegexValidator
from django.db import models
from ads.models import Advertisement


class Lead(models.Model):
    first_name = models.CharField("Имя", max_length=80)
    last_name = models.CharField("Фамилия", max_length=80)
    phone = models.CharField(
        "Телефон", max_length=20,
        validators=[RegexValidator(r"^[0-9+() -]+$", "Введите корректный номер телефона.")],
    )
    email = models.EmailField("Email")
    advertisement = models.ForeignKey(
        Advertisement, on_delete=models.PROTECT, related_name="leads", verbose_name="Рекламная кампания"
    )

    class Meta:
        verbose_name = "потенциальный клиент"
        verbose_name_plural = "потенциальные клиенты"
        ordering = ("last_name", "first_name")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
