import json

class HousingEncoder(json.JSONEncoder):
    
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)