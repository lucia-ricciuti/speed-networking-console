from .meeting import *

__all__ = ['GROUP_SIZE', 'create_groups']

GROUP_SIZE = 3

def create_groups(names, group_size=GROUP_SIZE):
    meeting_container = MeetingContainer()

    def inner():
        groups = []

        group = []
        available_names = names.copy()
        while len(available_names) > 0:
            name = available_names[0]
            # print('Current name is:', name)
            if len(group) == 0 or len(available_names) <= group_size:
                group.append(name)
                available_names.remove(name)
            else:
                target_with_max_value = {}
                for target in available_names:
                    target_with_max_value[target] = \
                        meeting_container.get_max_value_by_group_and_target(group, target)
                best_target = min(target_with_max_value, key=target_with_max_value.get)
                group.append(best_target)
                available_names.remove(best_target)

            if len(group) == group_size or len(available_names) == 0:
                # print('Appending group:', group)
                groups.append(group)
                meeting_container.add_group(group)
                group = []

        return groups, meeting_container
    return inner


