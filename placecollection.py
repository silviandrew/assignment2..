"""..."""


# Create your PlaceCollection class in this file

from place import Place


class PlaceCollection:
    def __init__(self, places = []):
        self.places = places

    def load_places(self, filename):
        open_file = open(filename, "r")
        all_lines = open_file.readlines()
        for line_index in range(len(all_lines)):
            sections = all_lines[line_index].strip().split(',')
            place = Place(sections[0], sections[1], int(sections[2]), sections[3] == 'v')
            self.places.append(place)

    def add_place(self, place):
        self.places.append(place)

    def sort(self, key):
        attrs = [key, 'priority']
        self.places.sort(key = lambda k: [ getattr(k, attr) for attr in attrs ])

    def dump_places_to_file(self, file):
        open_file = open(file, "w")
        outputs = []
        for place_index in range(len(self.places)):
            if self.places[place_index].is_visited:
                output_line = self.places[place_index].name + ',' + self.places[place_index].country + ',' + str(self.places[place_index].priority) + ',v\n'
            else:
                output_line = self.places[place_index].name + ',' + self.places[place_index].country + ',' + str(self.places[place_index].priority) + ',n\n'
            outputs.append(output_line)
        open_file.writelines(outputs)

    def count_number_of_unvisited(self):
        cnt = 0
        for place_index in range(len(self.places)):
            if not self.places[place_index].is_visited:
                cnt += 1
        return cnt
