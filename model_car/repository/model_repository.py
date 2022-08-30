from model_car.models import ModelCar


class ModelCarRepository:
    @staticmethod
    def find_all():
        return ModelCar.objects.all()

    @staticmethod
    def find_by_type(type):
        try:
            return ModelCar.objects.get(type_model=type)
        except:
            return None

    @staticmethod
    def find_by_pk(pk):
        try:
            return ModelCar.objects.get(id=pk)
        except:
            ...
        return None
