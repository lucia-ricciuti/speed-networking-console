from collections import namedtuple

Meeting = namedtuple('Meeting', ('name1', 'name2'))
Meeting.__doc__ = 'This class represents 2 persons that meet in the groups'
Meeting.name1.__doc__ = 'Name of the 1st person'
Meeting.name2.__doc__ = 'Name of the 2nd person'
# TODO add method for constructing an instance with the sorted names.

class MeetingContainer:

    def __init__(self):
        self.meetings = {}

    @staticmethod
    def _get_sorted_tuple(name1, name2):
        return tuple(sorted((name1,name2)))

    def add(self, name1, name2):
        t = self._get_sorted_tuple(name1, name2)
        value = self.meetings.get(t, 0)
        self.meetings[Meeting(*t)] = value + 1

    def add_group(self, group: 'list of names'):
        if len(group) < 2:
            pass
        available_names = group.copy()
        for name1 in group:
            available_names.remove(name1)
            for name2 in available_names:
                self.add(name1, name2)

    def get_min_value_meeting(self, target):
        return min(
            dict(filter(lambda e: target in (e[0].name1, e[0].name2), self.meetings.items())),
            key=self.meetings.get, default=None)

    def get_max_value_by_group_and_target(self, group, target):

        return max(map(
            lambda m: self.meetings.get(m, 0),
            filter(
                lambda m: target in m,
                filter(
                    lambda m: m.name1 in group or m.name2 in group,
                    self.meetings.keys())
            )
        ), default=0)

    def display(self):
        for e in dict(sorted(self.meetings.items(), key=lambda e: e[1], reverse=True)).items():
            print("{0} and {1} have met {2} times".format(e[0].name1, e[0].name2, e[1]))

