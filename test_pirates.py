import pytest
from Pirates_CRUD_Demo import validate_name, validate_parrot, Sailor

# validate_name tests:
def test_name_letters():
    review = "John"
    got = validate_name(review)
    expected = True
    assert got == expected

def test_name_number_str():
    review = "1"
    got = validate_name(review)
    expected = False
    assert got == expected

def test_name_too_long():
    review = "thisistolongname"
    got = validate_name(review)
    expected = False
    assert got == expected

def test_name_empty():
    review = ""
    got = validate_name(review)
    expected = False
    assert got == expected

def test_name_spec_sign():
    review = "!@#%^&()"
    got = validate_name(review)
    expected = True
    assert got == expected

# validate_parrot tests:
def test_parrot_str():
    review = "string"
    got = validate_parrot(review)
    expected = False
    assert got == expected

def test_parrot_int_str_zero():
    review = "012"
    for i in review:
        got = validate_parrot(i)

        expected = True
        assert got == expected

def test_parrot_int_str_many():
    review = "3456789"
    got = validate_parrot(review)
    expected = False
    assert got == expected

# sailor tests:
def test_add_crew_member_correct():
    sailor_name = "John"
    sailor_age="20"
    sailor_limbs="4"
    sailor_eyes="2"
    sailor_parrot="0"
    sailor_proffesion="s"
    sailor_sailing="5"


    sailor = Sailor()
    sailor.name = sailor_name
    sailor.age = sailor_age
    sailor.limbs = sailor_limbs
    sailor.eyes = sailor_eyes
    sailor.parrot = sailor_parrot
    sailor.proffesion = sailor_proffesion
    sailor.sailing = sailor_sailing

    got = sailor.__repr__()
    expected = "Sailor(num=0,name='John', age='20', limbs='4', eyes='2', parrot='0', proffesion='s', sailing='5', fighting=0, cost=0)"

    assert got == expected
