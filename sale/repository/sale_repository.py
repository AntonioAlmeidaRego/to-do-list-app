from sale.models import Sale


class SaleRepository:
    @staticmethod
    def find_by_all():
        return Sale.objects.all()

    @staticmethod
    def find_many_by_owner(pk):
        return Sale.objects.filter(owner__id=pk)

    @staticmethod
    def count():
        return len(SaleRepository.find_by_all())
