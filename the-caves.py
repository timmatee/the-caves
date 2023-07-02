# Mountains ASCII image.
print('''
 ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
 ********************************************************************************
''')

# Intro to the game
print("Welcome to the Caves.")
print("Your mission is to escape the Caves.")


# Sequence of choices for the user to pick with determined outcomes using nested if/elif/else conditonal statements.
first_choice = input(
    'You\'re at a crossroad, which way do you want to go? Type "left" or "right".\n').lower()

if first_choice == "left":
    second_choice = input(
        'You\'ve come to a platform with a bridge and a zipline. Type "zipline" or "walk".\n').lower()
    if second_choice == "walk":
        third_choice = input(
            'You\'ve arrived at a lake with a island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim across.\n').lower()
        if third_choice == "wait":
            final_choice = input(
                'You arrived at the island unharmed. There is a house with 3 doors. One red, one blue and one green. Which colour do you choose?\n').lower()
            if final_choice == "green":
                print("You go through the door and see your family and friends waving at you so you run towards them, only for them to transform into munnmies and you get mummified! Game Over")
            elif final_choice == "red":
                print(
                    "It's a room with a neverending black hole that has you in a continious loop of entering the room. Game Over.")
            elif final_choice == "blue":
                print('The room has a big red button labelled "Go Home". You press the button and in a flash you\'re back home. You Win! Or did you???????')
            else:
                print("You didn't pick one of the doors in front of you. Game Over.")

    else:
        print("At the end of the zipline, a gargoyle disfigured your body. Game Over.")
else:
    print("Walked through a portal that teleported you to a new dimension. Now you are stuck there forever. Game Over.")
