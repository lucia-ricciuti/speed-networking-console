from unittest import TestCase
from meeting import *

class TestMeetingContainer(TestCase):

    def setUp(self):
        self.meeting_container = MeetingContainer()

    def test_add(self):
        self.meeting_container.add('Mario', 'Lucia')
        self.meeting_container.display()
        self.meeting_container.add('Lucia', 'Mario')
        self.meeting_container.display()
        self.meeting_container.add('Lucia', 'Giovanni')
        self.meeting_container.display()

    def test_add_group(self):
        group = ['Lucia', 'Mario', 'Giovanni']
        self.meeting_container.add_group(group)
        self.meeting_container.display()

    def test_get_min_value_meeting(self):
        self.meeting_container.add('Mario', 'Lucia')
        self.meeting_container.add('Lucia', 'Mario')
        self.meeting_container.add('Lucia', 'Giovanni')
        m = self.meeting_container.get_min_value_meeting('Mariano')
        print(m)

    def test_get_max_value_by_group_and_target(self):
        self.meeting_container.add('Mario', 'Lucia')
        self.meeting_container.add('Lucia', 'Giovanni')
        self.meeting_container.add('Mariano', 'Lucia')
        self.meeting_container.add('Mariano', 'Lucia')
        self.meeting_container.add('Mariano', 'Giovanni')
        m = self.meeting_container.get_max_value_by_group_and_target(
            ('Lucia', 'Giovanni'), 'Mariano')
        print(m)
