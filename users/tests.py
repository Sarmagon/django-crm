from django.contrib.auth.models import Group
from django.core.management import call_command
from django.test import TestCase


class SeedRolesTests(TestCase):
    def test_command_creates_all_crm_roles(self):
        call_command("seed_roles")
        self.assertTrue(Group.objects.filter(name="Оператор").exists())
        self.assertTrue(Group.objects.filter(name="Маркетолог").exists())
        self.assertTrue(Group.objects.filter(name="Менеджер").exists())
