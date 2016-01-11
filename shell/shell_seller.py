from orcamentos.core.models import Seller, Employee

employee = Employee.objects.get(pk=5)  # jose
Seller.objects.create(
    employee=employee,
    internal=False,
    commissioned=True,
    commission=0.01
)

employee = Employee.objects.get(pk=8)  # regis
Seller.objects.create(
    employee=employee,
    internal=True,
    commissioned=True,
    commission=0.01
)

employee = Employee.objects.get(pk=9)  # adailton
Seller.objects.create(
    employee=employee,
    internal=True,
    commissioned=True,
    commission=0.01
)
