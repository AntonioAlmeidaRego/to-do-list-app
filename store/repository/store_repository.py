from store.models import Store


class StoreRepository:
    name = 'Carford'

    @staticmethod
    def find_by_name(name):
        try:
            return Store.objects.get(name=name)
        except:
            return None

    @staticmethod
    def create_or_get(name=None):
        name = StoreRepository.check_name(name)
        store = StoreRepository.find_by_name(name)
        if not store:
            store = Store()
            store.name = name
            store.save()
        return store

    @staticmethod
    def check_name(name=None):
        if name: return name
        return StoreRepository.name
