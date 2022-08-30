from store.models import Store


class StoreRepository:
    @staticmethod
    def find_by_name(name):
        try:
            return Store.objects.get(name=name)
        except:
            return None

    @staticmethod
    def create_or_get(name):
        store = StoreRepository.find_by_name(name)
        if not store:
            store = Store()
            store.name = name
            store.save()
        return store
