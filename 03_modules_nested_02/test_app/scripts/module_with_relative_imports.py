from .greetings import greetings
from ..data import load_raw_data
from ..models import Person

data = load_raw_data()
people = [Person(name) for name in data]

for person in people:
    print(greetings(person.name))

