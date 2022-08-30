from color.models import Color


class ColorRepository:
    @staticmethod
    def find_all():
        return Color.objects.all()

    @staticmethod
    def find_by_pk(pk):
        try:
            return Color.objects.get(id=pk)
        except:
            ...
        return None

    @staticmethod
    def find_by_type(type):
        try:
            return Color.objects.get(type_color=type)
        except:
            return None
