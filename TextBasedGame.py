# Carisma Carter

# function
def show_instructions():
    # print a main menu and the commands
    print("Bowser Text Wild Adventures Game")
    print("Collect 6 items to win the game, or be eaten by Bowser.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def player_stats():
    global current_room
    global inventory
    print('_' * 20)
    print('You are in the {}'.format(current_room))
    print('Inventory: ' + str(inventory))
    if 'item' in rooms[current_room]:
        print('You see ' + rooms[current_room]['item'])
    print('_' * 20)


# In this solution, the player’s status would be shown in a separate function.
# You may organize your functions differently

# A dictionary linking a room to other rooms
# and linking one item for each room except the Start room (Front Office) and the room containing the villain

rooms = {
    'Front Office': {'name': 'Front Office', 'West': 'Teacher Lounge', 'item': 'Sword', 'South': 'Auditorium'},
    'Teacher Lounge': {'name': 'Teacher Lounge', 'East': 'Front Office'},
    'Playground': {'name': 'Playground', 'item': 'Helmet', 'East': 'Auditorium'},
    'Auditorium': {'name': 'Auditorium', 'East': 'Gymnasium', 'North': 'Cafeteria'},
    'Theater': {'name': 'Theater', 'item': 'Full body Armor', 'North': 'Auditorium'},
    '5th Grade Classroom': {'name': '5th Grade Classroom', 'item': 'Time Warp', 'West': 'Theater'},
    'Cafeteria': {'name': 'Cafeteria', 'item': 'Snack', 'South': 'Gymnasium', 'West': 'Auditorium'},
    'Gymnasium': {'name': 'Gymnasium', 'item': 'Bowser', 'West': 'Auditorium'},  # villain room
    'Exit': {'name': 'Exit'}

}

global current_room
current_room = 'Front Office'  # start room
global inventory
inventory = []
show_instructions()


def main():
    global current_room
    global inventory
    player_stats()
    player_move = ''
    while player_move == '':
        player_move = input('Enter your move:\n').title()
    if player_move == 'Go North' or player_move == 'Go South' or player_move == 'Go East' or player_move == 'Go West':
        player_move = player_move[3:]
        if player_move not in rooms[current_room]:
            print('Invalid direction. Try again.')
        else:
            current_room = rooms[current_room][player_move]
    elif player_move[0:3] == 'Get':
        if 'item' not in rooms[current_room] or player_move[4:] not in rooms[current_room]['item']:
            print('Can\'t get {}!'.format(player_move[4:]))
        else:
            inventory += [player_move[4:]]
            print(player_move[4:] + ' retrieved!')
            del rooms[current_room]['item']

    if current_room == 'Gymnasium':
        print('AHHGGG...GAME OVER!')
        exit(0)

    if len(inventory) == 7:
        print('Congratulations! You have collected all items and defeated the Great Bowser !!!')
        exit(0)

    if player_move == 'Exit':
        print('Come back and Play again soon!')
        exit(0)


while True:
    main()
