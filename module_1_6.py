my_dict = {"Roman": 1987, "Katerina": 1988}
print(my_dict)
print(my_dict["Roman"])
print(my_dict.get("Mark"))
my_dict["Olga"] = 2010
print(my_dict)
my_dict.update({"Ksenia":2014,"Maria":2021})
print(my_dict)
a = my_dict.pop("Olga")
print(my_dict)
print(a)


my_set = {1,2,1,2,3,4,5,5,4,3,3,}
print(my_set)
print(my_set.add(6), my_set.add(7))
print(my_set)
print(my_set.discard(4))
print(my_set)


