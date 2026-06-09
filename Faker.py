from faker import Faker

for _ in range(10):
    faker = Faker('RU')

    name = faker.name()
    address = faker.address()
    email = faker.email()
    job = faker.job()

    print(
        f'__________\n'
        f'{name}\n'
        f'{address}\n'
        f'{email}\n'
        f'{job}'
    )
