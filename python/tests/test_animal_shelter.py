from code_challenges.fifo_animal_shelter.fifo_animal_shelter import Node , AnimalShelter


def test_enqueue():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')

    actual = str(shelter)
    expected = 'cat -> dog -> cat -> Null'
    assert actual == expected

def test_dequeue_with_param():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')

    shelter.dequeue('dog')

    actual = str(shelter)
    expected = 'cat -> cat -> dog -> Null'
    assert actual == expected

def test_dequq_without_param():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')

    shelter.dequeue()
    actual = str(shelter)
    expected = 'dog -> cat -> dog -> Null'
    assert actual == expected