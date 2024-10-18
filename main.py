"""
    The goal of this app is to create groups for a speed networking session.
"""

import argparse

from logic import *

# List of the names of the people to group.
names = ['Lucia', 'Antonio', 'Mario', 'Sandro', 'Giulia', 'Carlo', 'Benedetta', 'Nicola', 'Roberto']

if __name__ == '__main__':
    print("Running Speed Networking")
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument('-s', '--group-size',
                           type=int,
                           default=GROUP_SIZE,
                           help='Number of names in each group.')
    args = argparser.parse_args()
    print(args)

    create_groups_func = create_groups(names, args.group_size)

    for i in range(3):
        print("\nRound #",i)
        groups, meeting_container = create_groups_func()
        print(groups)
        for e in dict(filter(lambda e: e[1] > 1, meeting_container.meetings.items())).items():
            print("{0} and {1} have met {2} times".format(e[0].name1, e[0].name2, e[1]))
