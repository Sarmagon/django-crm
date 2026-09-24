from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


ROLE_PERMISSIONS = {
    "Оператор": [
        "leads.add_lead", "leads.change_lead", "leads.delete_lead", "leads.view_lead",
        "ads.view_advertisement",
    ],
    "Маркетолог": [
        "products.add_product", "products.change_product", "products.delete_product", "products.view_product",
        "ads.add_advertisement", "ads.change_advertisement", "ads.delete_advertisement", "ads.view_advertisement",
    ],
    "Менеджер": [
        "leads.view_lead",
        "contracts.add_contract", "contracts.change_contract", "contracts.delete_contract", "contracts.view_contract",
        "customers.add_customer", "customers.change_customer", "customers.delete_customer", "customers.view_customer",
        "ads.view_advertisement",
    ],
}


class Command(BaseCommand):
    help = "Создаёт преднастроенные роли CRM и назначает им разрешения."

    def handle(self, *args, **options):
        for role_name, permission_names in ROLE_PERMISSIONS.items():
            group, _ = Group.objects.get_or_create(name=role_name)
            permissions = []
            for permission_name in permission_names:
                app_label, codename = permission_name.split(".")
                permissions.append(Permission.objects.get(
                    content_type__app_label=app_label, codename=codename
                ))
            group.permissions.set(permissions)
            self.stdout.write(self.style.SUCCESS(f"Роль «{role_name}» настроена."))
