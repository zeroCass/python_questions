import importlib

'''
Programa teste:
-Importa classes presentes em modulos
'''


module = importlib.import_module('some_class')
class_name = 'Instance'
instance_class = getattr(module, class_name)

i = instance_class()
print(i.x)
