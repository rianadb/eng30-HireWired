from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, contact_number=None, **extra_fields):
        if not username:
            raise ValueError("Username must be set.")
        if not password:
            raise ValueError("Password must be set.")
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email or "", contact_number=contact_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_worker(self, username, password, email=None, contact_number=None, **extra_fields):
        return self.create_user(username=username, password=password, contact_number=contact_number, user_type='worker', **extra_fields)

    def create_employer(self, username, email, password, contact_number=None, **extra_fields):
        if not email:
            raise ValueError("Employers must have an email address")
        return self.create_user(username=username, email=email, password=password, contact_number=contact_number, user_type='employer', **extra_fields)

    def create_superuser(self, username, email, password, contact_number=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, email, password, contact_number, **extra_fields)