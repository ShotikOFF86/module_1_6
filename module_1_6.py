my_dict = {"Жора"  : 1986, "Татьяна" : 1990, "Феофан" : 1900}
print(my_dict)
print(my_dict ["Феофан"])
print(my_dict.get("Василий", "Значение не найдено"))
my_dict.update({"Станислав" : 1985, "Ольга" : 2000})
print(my_dict)
e = my_dict.pop("Татьяна")
print(my_dict)
print(e, "Удалнное значение")
print(my_dict)
my_set = {1,1,2,2,3,4,5, "String", (1,2,3,4)}
print(my_set)
my_set.add("Strike")
print(my_set)