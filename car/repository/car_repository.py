from car.models import Car


class CarRepository:
    @staticmethod
    def find_all():
        return Car.objects.all()

    @staticmethod
    def find_pk(pk):
        try:
            return Car.objects.get(id=pk)
        except:
            ...
        return None
