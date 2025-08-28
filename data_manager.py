from tinydb import Query, TinyDB
from tinydb.storages import JSONStorage

class PrettyJSONStorage(JSONStorage):
    """Class modifying indent value of JSONStorage to 4 in order to make it prettier"""
    def __init__(self, *args, **kwargs):
        kwargs['indent'] = 4
        super().__init__(*args, **kwargs)


class DataManager:
    """Data manager class for TinyDB database."""
    def __init__(self):
        self.best_value = TinyDB("best_value.json", storage=PrettyJSONStorage)
        self.data_set1 = TinyDB("data_set1.json", storage=PrettyJSONStorage)
        self.data_set2 = TinyDB("data_set2.json", storage=PrettyJSONStorage)
    
    def save(self, result, storage="best_value.json"):
        if storage == "best_value.json":
            self.best_value.insert(result)
        elif storage == "data_set1.json":
            self.data_set1.insert(result)
        elif storage == "data_set2.json":
            self.data_set2.insert(result)
        else:
            raise ValueError("Passed storage config doesn't exist")
