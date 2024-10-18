from unittest import TestCase
from logic.meeting import *

class TestMeetingContainer(TestCase):

    def setUp(self):
        self.meeting_container = MeetingContainer()

    def test_add_group(self):
        group = ['Lucia', 'Mario', 'Giovanni']
        self.meeting_container.add_group(group)
        self.meeting_container.display()
        assert len(self.meeting_container.meetings) == 3

    def test_get_min_value_meeting(self):
        self.meeting_container.add('Mario', 'Lucia')
        self.meeting_container.add('Lucia', 'Mario')
        self.meeting_container.add('Lucia', 'Giovanni')
        m = self.meeting_container.get_min_value_meeting('Lucia')
        print(m)
        assert m == Meeting('Giovanni', 'Lucia')

    def test_get_max_value_by_group_and_target(self):
        self.meeting_container.add('Mario', 'Lucia')
        self.meeting_container.add('Lucia', 'Giovanni')
        self.meeting_container.add('Mariano', 'Lucia')
        self.meeting_container.add('Mariano', 'Lucia')
        self.meeting_container.add('Mariano', 'Giovanni')
        m = self.meeting_container.get_max_value_by_group_and_target(
            ('Lucia', 'Giovanni'), 'Mariano')
        print(m)
