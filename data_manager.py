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
        self.best_result = TinyDB("best_value.json", storage=PrettyJSONStorage)
    
    def save(self, result):
        self.best_result.insert(result)
