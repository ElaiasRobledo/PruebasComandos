mi_diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

mi_diccionario.get("c")
3

mi_diccionario.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

mi_diccionario.keys()
dict_keys(['a', 'b', 'c', 'd'])

mi_diccionario.pop("d")
4

mi_diccionario.popitem()
('c', 3)

mi_diccionario.setdefault("a", 15)
1

mi_diccionario
{'a': 1, 'b': 2}