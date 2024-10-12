from meeting import *

GROUP_SIZE = 3

# List of the names of the people to group.
names = ['Lucia', 'Antonio', 'Mario', 'Sandro', 'Giulia', 'Carlo', 'Benedetta', 'Nicola', 'Roberto']

meeting_container = MeetingContainer()

def create_groups(names, meeting_container, GROUP_SIZE):

    groups = []

    group = []
    available_names = names.copy()
    while len(available_names) > 0:
        name = available_names[0]
        # print('Current name is:', name)
        if len(group) == 0 or len(available_names) <= GROUP_SIZE:
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

        if len(group) == GROUP_SIZE or len(available_names) == 0:
            # print('Appending group:', group)
            groups.append(group)
            meeting_container.add_group(group)
            group = []

    return groups

groups = create_groups(names, meeting_container, GROUP_SIZE)
print(groups)

groups = create_groups(names, meeting_container, GROUP_SIZE)
print(groups)

groups = create_groups(names, meeting_container, GROUP_SIZE)
print(groups)

groups = create_groups(names, meeting_container, GROUP_SIZE)
print(groups)

meeting_container.display()
