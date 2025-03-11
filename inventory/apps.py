from django.apps import AppConfig

class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"

    # def ready(self):
    #     from django.db.utils import OperationalError, ProgrammingError
    #     """
    #     Ensures that roles and permissions are created every time the app starts.
    #     """
    #     try:
    #         # Ensure permissions exist before assigning them
    #         self.create_missing_permissions()

    #         # Assign permissions to roles
    #         self.create_roles_and_permissions()

    #     except (OperationalError, ProgrammingError):
    #         print("Database is not ready yet. Skipping role creation.")

    def create_missing_permissions(self):
        from django.contrib.auth.models import Permission
        from django.contrib.contenttypes.models import ContentType
        
        from django.core.management import call_command
    
        """
        Ensures all required permissions exist before assigning them.
        """
        # Run Django command to refresh permissions
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)

        # Define the models and permissions
        permissions = {
            "product": ["add", "change", "delete", "view"],
            "inventorytransaction": ["add", "change", "delete", "view"],
            "order": ["add", "change", "delete", "view"],
            "supplier": ["add", "change", "delete", "view"],
            "report": ["add", "view", "delete"],
        }

        # Ensure permissions exist
        for model, actions in permissions.items():
            content_type, _ = ContentType.objects.get_or_create(
                app_label="inventory", model=model
            )
            for action in actions:
                codename = f"{action}_{model}"
                Permission.objects.get_or_create(
                    codename=codename,
                    content_type=content_type,
                    defaults={"name": f"Can {action} {model}"},
                )

    def create_roles_and_permissions(self):
        from django.contrib.auth.models import Group, Permission
        """
        Assigns permissions to roles and ensures all roles exist.
        """
        roles = {
            "Admin": [
                "add_product", "change_product", "delete_product", "view_product",
                "add_inventorytransaction", "change_inventorytransaction", "delete_inventorytransaction", "view_inventorytransaction",
                "add_order", "change_order", "delete_order", "view_order",
                "add_supplier", "change_supplier", "delete_supplier", "view_supplier",
                "view_report", "add_report", "delete_report"
            ],
            "Manager": [
                "view_product", "change_product",
                "view_inventorytransaction", "change_inventorytransaction",
                "view_order", "change_order",
                "view_report"
            ],
            "Staff": [
                "view_product", "view_inventorytransaction",
                "view_order"
            ],
            "Warehouse Worker": [
                "view_product", "add_inventorytransaction", "view_inventorytransaction"
            ]
        }

        for role_name, permissions in roles.items():
            group, _ = Group.objects.get_or_create(name=role_name)
            for perm_codename in permissions:
                permission, created = Permission.objects.get_or_create(codename=perm_codename)
                group.permissions.add(permission)
