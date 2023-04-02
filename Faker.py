from faker import Faker


faker = Faker('RU')

name = faker.name()
address = faker.address()
email = faker.email()
job = faker.job()

print(
    f'{name}\n'
    f'{address}\n'
    f'{email}\n'
    f'{job}'
)
