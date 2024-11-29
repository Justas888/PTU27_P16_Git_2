person = {
    "name": "Albert",
    "age": 60,

}

for elem in person:  # gausim tik raktus
    print(elem)
#rodinių metodai
#  .items() - pilnas rodinys raktai - reikšmės
print(person.items())  #  dict_items([('name', 'Albert'), ('surname', 'Einstein'), ('age', 60)])

for key, value in person.items():
    print(key, value)


# .key() - tik raktai
for key in person.keys():
    print(key)

for elem in person:  # gausim tik raktus, nes keys() iškviečiamas pagal nutylėjimą
    print(elem)

