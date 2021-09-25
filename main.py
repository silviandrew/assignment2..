"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from placecollection import PlaceCollection
from place import Place
from kivy.uix.button import Button
from kivy.lang import Builder

class TravelTrackerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_sort = "Sort by:"
        self.label_add_place = "Add New Place..."
        self.label_name = "Name:"
        self.label_country = "Country:"
        self.label_priority = "Priority:"
        self.button_add_place = 'Add Place'
        self.button_clear = 'Clear'
        self.default_selected_item = "is_visited"
        self.all_keys = ['is_visited', 'name', 'country', 'priority']
        self.visit_suffix = ' (visited)'
        self.warning_empty = "All fields must be completed"
        self.warning_priority_not_digit = "Please enter a valid number"
        self.warning_priority_gt_zero = "Priority must be > 0"
        self.place_file_name = 'places.csv'
        self.places_to_visit = 'Places to visit: '
        self.need_to_visit = 'You need to visit '
        self.have_visited = 'You visited '
        self.important_suffix_unvisited = 'Get going!'
        self.important_suffix_visited = 'Great travelling!'
        self.mapping = {}

        self.placecollection = PlaceCollection()
        self.placecollection.load_places(self.place_file_name)

    def build(self):
        self.root = Builder.load_file('app.kv')
        self.title = "Assignment 2 – Travel Tracker 2.0"
        self.refresh_place_data()
        return self.root


    def refresh_place_data(self):
        self.root.ids.places_layout_id.clear_widgets()
        key_name = self.root.ids.spinner_sort.text
        self.placecollection.sort(key_name)
        unvisited_number = self.placecollection.count_number_of_unvisited()
        self.root.ids.label_visit.text = self.places_to_visit + str(unvisited_number)
        places = self.placecollection.places

        for id in range(len(places)):
            self.mapping[str(places[id])] = places[id]
            place_button = Button(text=str(places[id]))
            if not places[id].is_visited:
                place_button.background_color = '#00FF00'
            else:
                place_button.text += self.visit_suffix
            place_button.bind(on_release=self.add_place_button)
            self.root.ids.places_layout_id.add_widget(place_button)

    def add_place(self):
        try:
            if not self.root.ids.name_id.text or \
                    not self.root.ids.country_id.text or \
                    not self.root.ids.priority_id.text:
                raise Exception(self.warning_empty)
            elif not self.root.ids.priority_id.text.isdigit():
                raise Exception(self.warning_priority_not_digit)
            elif int(self.root.ids.priority_id.text) < 1:
                raise Exception(self.warning_priority_gt_zero)
            else:
                place = Place(self.root.ids.name_id.text, self.root.ids.country_id.text, int(self.root.ids.priority_id.text))
                self.placecollection.add_place(place)
                self.clear_all_inputs()
                self.refresh_place_data()
        except Exception as error:
            self.root.ids.label_info.text = str(error)

    def clear_all_inputs(self):
        self.root.ids.name_id.text = \
            self.root.ids.country_id.text =\
            self.root.ids.priority_id.text = ''

    def add_place_button(self, instance):
        get_button_text = instance.text.replace(self.visit_suffix,'')
        get_selected_place = self.mapping[get_button_text]
        place = self.find_place(get_selected_place)
        if place:
            visited = place.is_visited
            important = place.check_priority_important()
            if not visited and important:
                self.root.ids.label_info.text = self.need_to_visit + place.name + '.' + self.important_suffix_unvisited
            elif not visited and not important:
                self.root.ids.label_info.text = self.need_to_visit + place.name + '.'
            elif visited and important:
                self.root.ids.label_info.text = self.have_visited + place.name + '.' + self.important_suffix_visited
            elif visited and not important:
                self.root.ids.label_info.text = self.have_visited + place.name + '.'
            self.refresh_place_data()

    def find_place(self, get_selected_place):
        places = self.placecollection.places
        for id in range(len(places)):
            if places[id].name == get_selected_place.name and \
                    places[id].country == get_selected_place.country and \
                    places[id].priority == get_selected_place.priority:
                if places[id].is_visited:
                    places[id].change_to_unvisited()
                else:
                    places[id].change_to_visited()
                return places[id]
        return None


    def on_stop(self):
        self.placecollection.dump_places_to_file(self.place_file_name)


if __name__ == '__main__':
    TravelTrackerApp().run()
