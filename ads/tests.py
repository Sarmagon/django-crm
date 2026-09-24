from decimal import Decimal
from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from ads.models import Advertisement
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead
from products.models import Product


class AdvertisementStatisticsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin", password="test-password"
        )
        product = Product.objects.create(
            name="CRM-настройка", description="Настройка системы", cost=Decimal("500.00")
        )
        advertisement = Advertisement.objects.create(
            name="Поисковая реклама", product=product, channel="Поиск", budget=Decimal("250.00")
        )
        lead = Lead.objects.create(
            first_name="Иван", last_name="Иванов", phone="+79990000000",
            email="ivan@example.com", advertisement=advertisement,
        )
        contract = Contract.objects.create(
            name="Договор с Ивановым", product=product, start_date=date.today(),
            end_date=date(2030, 1, 1), cost=Decimal("500.00"),
        )
        Customer.objects.create(lead=lead, contract=contract)

    def test_statistics_show_leads_customers_and_ratio(self):
        self.client.force_login(self.user)
        response = self.client.get("/ads/statistic/")
        self.assertContains(response, "Лидов: 1")
        self.assertContains(response, "Активных клиентов: 1")
        self.assertContains(response, "2")
