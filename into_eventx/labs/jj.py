from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle

class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}

def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct


data = [1,2,3, set(['knights', 'who', 'say', 'ni']), {'key':'value'}]
j = dumps(data, cls=PythonObjectEncoder)
print loads(j, object_hook=as_python_object)

print j[0]
