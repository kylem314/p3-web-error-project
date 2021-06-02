#  Play Game
os.system('clear')
print_board(board_display)

for turn in range(num_turns):
    print("Turn:", turn + 1, "of", num_turns)
    print("Ships left:", len(ship_list))
    print()

    guess_coords = {}
    while True:
        guess_coords['row'] = get_row()
        guess_coords['col'] = get_col()
        if board_display[guess_coords['row']][guess_coords['col']] == 'X' or \
                board_display[guess_coords['row']][guess_coords['col']] == '*':
            print("\nYou guessed that one already.")
        else:
            break

    os.system('clear')

    #shot guessing
    ship_hit = False
    for ship in ship_list:
        #hits
        if ship.contains(guess_coords):
            print("Hit!")
            ship_hit = True
            board_display[guess_coords['row']][guess_coords['col']] = 'X'
            if ship.destroyed():
                print("Ship Destroyed!")
                ship_list.remove(ship)
            break
    #misses
    if not ship_hit:
        board_display[guess_coords['row']][guess_coords['col']] = '*'
        print("You missed!")

    print_board(board_display)

    if not ship_list:
        break

# End Game
if ship_list:
    print("You lose!")
else:
    print("All the ships are sunk. You win!")


