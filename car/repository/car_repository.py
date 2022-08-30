from car.models import Car


class CarRepository:
    @staticmethod
    def find_all():
        return Car.objects.all()

    @staticmethod
    def count():
        return len(Car.objects.all())

    @staticmethod
    def find_by_last():
        return Car.objects.all().order_by('-created_at').first()

    @staticmethod
    def find_pk(pk):
        try:
            return Car.objects.get(id=pk)
        except:
            ...
        return None
