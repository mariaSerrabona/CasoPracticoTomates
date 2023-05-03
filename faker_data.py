import csv
from faker import Faker

registros=10000
fake=Faker()

def create_csv_file():
    with open('./tomates.csv', 'w') as csvfile:
        fieldnames=['tipo_cultivo', 'ubicacion', 'tamanio', 'rdto', 'uso_fertilizantes']

        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        tipo_cultivo=['rastrera', 'semierecta', 'erecta']

        for i in range (registros):
            writer.writerow(
                {
                    'tipo_cultivo':fake.sentence(nb_words=1, ext_word_list=tipo_cultivo),
                    'ubicacion':fake.random_int(min=1000, max=2000),
                    'tamanio':fake.random_int(min=100, max=100000),
                    'rdto':fake.random_number(digits=4)/10000,
                    'uso_fertilizantes':fake.boolean()

                }
            )



if __name__ =='__main__':
    create_csv_file()