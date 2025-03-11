from django.db import migrations

def recreate_permissions(apps, schema_editor):
    # Get models for groups and permissions
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Define roles and their associated permissions
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

    # Create roles and assign permissions
    for role_name, permissions in roles.items():
        group, created = Group.objects.get_or_create(name=role_name)
        for perm_codename in permissions:
            print(perm_codename)
            try:
                permission,created = Permission.objects.get_or_create(codename=perm_codename)
                print(permission)
                group.permissions.add(permission)
            except Permission.DoesNotExist:
                print(f"Permission {perm_codename} not found!")
                

def remove_roles_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    roles = ["Admin", "Manager", "Staff", "Warehouse Worker"]

    for role_name in roles:
        try:
            group = Group.objects.get(name=role_name)
            group.delete()
        except Group.DoesNotExist:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_initial'),  # Adjust this based on your actual initial migration file
    ]

    operations = [
        migrations.RunPython(recreate_permissions, remove_roles_and_permissions),
    ]
