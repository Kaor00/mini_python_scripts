from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender

person = Person(Locale.EN)

print(person.full_name())
print(person.email(domains=['yahoo.com']))
print(person.email(domains=["mimesys.com"], unique=True))
print(person.telephone(mask="1-5##-3##-2##9"))

de = Person(locale=Locale.DE)
en = Person(locale=Locale.EN)

print(de.full_name(gender=Gender.FEMALE))
print(en.full_name(gender=Gender.MALE))
