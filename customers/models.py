from django.db import models
from contracts.models import Contract
from leads.models import Lead


class Customer(models.Model):
    lead = models.OneToOneField(
        Lead, on_delete=models.PROTECT, related_name="customer", verbose_name="Потенциальный клиент"
    )
    contract = models.OneToOneField(
        Contract, on_delete=models.PROTECT, related_name="customer", verbose_name="Контракт"
    )
    created_at = models.DateTimeField("Дата перевода", auto_now_add=True)

    class Meta:
        verbose_name = "активный клиент"
        verbose_name_plural = "активные клиенты"
        ordering = ("lead__last_name", "lead__first_name")

    def __str__(self):
        return str(self.lead)
