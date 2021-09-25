"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)
    # TODO: Add more sorting tests
    print("Test sorting - name:")
    place_collection.sort("name")
    print(place_collection)

    print("Test sorting - is_visited:")
    place_collection.sort("is_visited")
    print(place_collection)

    # TODO: Test saving places (check CSV file manually to see results)
    place_collection.dump_places_to_file('places.dump.csv')

    # TODO: Add more tests, as appropriate, for each method
    assert place_collection.count_number_of_unvisited() == 3

    place_collection.add_place(Place("Test", "Australia", 5, False))

    assert place_collection.count_number_of_unvisited() == 4

run_tests()
