from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, identifier, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not identifier:
            raise ValueError('The given email or phone must be set')
        user = self.model(identifier=identifier, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, identifier, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('locale', 'en')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(identifier, password, **extra_fields)

    def create_superuser(self, identifier, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('locale', 'en')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(identifier, password, **extra_fields)
