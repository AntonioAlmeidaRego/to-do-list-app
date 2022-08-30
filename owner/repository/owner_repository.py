from owner.models import Owner


class OwnerRepository:
    @staticmethod
    def find_all():
        return Owner.objects.all()

    @staticmethod
    def find_by_last():
        return Owner.objects.all().order_by('-created_at').first()

    @staticmethod
    def count():
        return len(Owner.objects.all())

    @staticmethod
    def find_by_pk(pk):
        try:
            return Owner.objects.get(id=pk)
        except:
            return None

    @staticmethod
    def find_by_car(instance_car):
        try:
            return Owner.objects.get(cars__in=[instance_car])
        except:
            return None
