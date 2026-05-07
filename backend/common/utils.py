import secrets
import string

from auth.models import User

PASSWORD_LENGTH = 10


class CommonUtils:
    def _generate_random_password(self) -> str:
        chars = string.ascii_letters + string.digits
        generated_password = "".join(
            secrets.choice(chars) for _ in range(PASSWORD_LENGTH)
        )
        return generated_password

    def _create_username_with_pk(self, instance: User) -> str:
        return (
            f"{instance.first_name.lower()}_{instance.last_name.lower()}_{instance.pk}"
        )



utils = CommonUtils()

random_password = utils._generate_random_password
create_username = utils._create_username_with_pk
