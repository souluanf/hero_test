from django.contrib.auth import get_user_model
from django.db import models
from apps.company.models import Company

User = get_user_model()


class EmployeeManager(models.Manager):
    def create_employee(self, email, full_name, cpf, password):
        user = self.model(
            email=email,
            full_name=full_name,
            cpf=cpf
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Employee(User):
    full_name = models.CharField('Nome Completo', max_length=70)
    companies = models.ManyToManyField(Company, verbose_name='Empresas',
                                       related_name='Funcionarios')

    objects = EmployeeManager()

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionarios'
