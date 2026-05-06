from auth.models import User


def generate_unique_username(instance: User) -> str:
    return f"{instance.pk}_{instance.first_name.lower()}_{instance.last_name.lower()}"
