"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    assert new_place.name == "Malagar" and \
            new_place.country == "Spain" and \
            new_place.priority == 1 and \
            not new_place.is_visited

    # TODO: Add more tests, as appropriate, for each method
    new_place = Place("Malagar", "Spain", 2, False)
    assert new_place.check_priority_important()
    new_place = Place("Malagar", "Spain", 1, False)
    assert new_place.check_priority_important()
    new_place = Place("Malagar", "Spain", 3, False)
    assert not new_place.check_priority_important()

    new_place.change_to_visited()
    assert new_place.is_visited

    new_place.change_to_unvisited()
    assert not new_place.is_visited

    assert str(new_place) == "Malagar in Spain, priority 3"


run_tests()
