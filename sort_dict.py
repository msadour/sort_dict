def sort_dict(dict_no_sorted, by_what, sens="asc"):
	"""
	Cette fonction permet de trié le disctionnaire en parametre (dict_no_sorted).
	Elle trie les clés ou les valeur via l'argument "by_what". On peut egalement
	trié par ordre croissant (asc) ou decroissant (desc) via l'argument "sens".
	"""
  dict_sorted = {}
  if by_what == "key":
    lst_keys = sorted([key for key, value in dict_no_sorted.items()])
    if sens == "desc":
      lst_keys = reversed(lst_keys)
    for k in lst_keys:
      value_sorted = dict_no_sorted[k]
      dict_sorted[k] = value_sorted
  elif by_what == "value":
    lst_key_value = [[value, key] for key, value in dict_no_sorted.items()]
    lst_value = sorted([value for key,value in dict_no_sorted.items()])
    if sens == "desc":
      lst_value = reversed(lst_value)
    for v in lst_value:
      for kv in lst_key_value:
        if v in kv:
          dict_sorted[kv[1]] = v 
          lst_key_value.remove(kv)
  else:
    return {"Erreur" : "Veuillez saisir en parametre soit clé soit valeur !"}
  return dict_sorted


dict_test = {
  'd' : 4,
  'e' : 5,
  'b' : 2,
  'a' : 1,
  'c' : 3,
}

print("----------- non trié -----------  ")
print(dict_test)
print("----------- trié par clé -----------  ")
print(sort_dict(dict_test, "key", "desc"))
print("----------- trié par valeur -----------  ")
print(sort_dict(dict_test, "value", "desc"))