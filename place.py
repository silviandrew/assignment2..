"""..."""


# Create your Place class in this file


class Place:

    def __init__(self, name_param = "", country_param = "", priority_param = 0, is_visited_param = False):
        self.name = name_param
        self.country = country_param
        self.priority = int(priority_param)
        self.is_visited = is_visited_param

    def check_priority_important(self):
        important = False
        if 1 <= self.priority <= 2:
            important = True
        return important

    def change_to_visited(self):
        self.is_visited = True

    def change_to_unvisited(self):
        self.is_visited = False

    def __str__(self):
        return_str = self.name + ' in ' + self.country + ', priority ' + str(self.priority)
        return return_str
