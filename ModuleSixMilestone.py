# Carisma Carter

# dictionary that leads rooms to other rooms
rooms = {
    'Front Office': {'name': 'Front Office', 'West': 'Teacher Lounge'},
    'Teacher Lounge': {'name': 'Teacher Lounge', 'South': 'Auditorium'},
    'Auditorium': {'name': 'Auditorium', 'West': 'Playground', 'East': 'Auditorium', 'South': 'Theater'},
    'Theater': {'name': 'Theater', 'East': '5th Grade Classroom'},
    '5th Grade Classroom': {'name': '5th Grade Classroom', 'West': 'Theater', 'North': 'Auditorium'},
    'Cafeteria': {'name': 'Cafeteria', 'South': 'Gymnasium'},
    'Gymnasium': {'name': 'Gymnasium', 'West': 'Auditorium'},
    'Exit': {'name': 'Exit'}
}
directions = ['North', 'South', 'East', 'West']  # list of directions
current_room = rooms['Front Office']  # start room
while True:
    # display the current room
    print('You are in the {}'.format(current_room['name']))
    # getting user input
    command = input('\nIn what direction would you like to go?').title()
    if command == 'Exit':
        if current_room['name'] == 'Exit': break
        else:
            current_room = rooms[command]
            print('You are now in Exit room. Type Exit again to stop the game.')
    elif command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
    elif command == 'Quit':
        break
    else:  # invalid direction
        print("Invalid direction. Please try again.")
