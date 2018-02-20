

def display_board(current_positions):
    board = """
    {top left} | {top center} | {top right}
    ---------
    {center left} | {center} | {center right}
    ---------
    {bottom left} | {bottom center} | {bottom right}
    """.format(**current_positions)
    print(board)
def user_move(current_positions,current_player):
    

    possible_moves = []
    user_prompt ="plaese pick your move from the options below!"
    for position in current_positions:
        if current_positions[position] == " ":
            possible_moves.append(position)
            user_prompt += "\n" + position
    user_prompt += '\n'
    user_choice = raw_input(user_prompt).lower()
    while user_choice not in possible_moves:
        user_choice = raw_input(user_prompt).lower()
    current_positions[user_choice] =current_player
    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"
    return current_positions, current_player


def is_game_over(current_positions):
    winners = [["top left", "top center", "top right"],
              ["center left", "center", "center right"],
              ["bottom left", "bottom center", "bottom right"],
              ["top left", "center left", "bottom left"],
              ["top center", "center", "bottom center"],
              ["top right", "center right", "bottom right"],
              ["top left", "center", "bottom right"],
              ["top right", "center", "bottom left"]]
    possible_winner=""
    for winning_combo in winners:
        for value in winning_combo:
            possible_winner += current_positions[value]
            
        
        if possible_winner == "XXX":
            print "X"
            return "X" + " wins!"
        
        elif possible_winner == "000":
            return "0" + " wins!"
        possible_winner=""   

    is_draw =True
    for position in current_positions:
            if current_positions[position] == " ":
                is_draw =False
                return False
    if is_draw:
            return "Draw!"
def play_game():
    current_positions = {"top left": " ", "top center": " ", "top right": " ",
                     "center left": " ", "center": " ", "center right": " ",
                     "bottom left": " ", "bottom center": " ", "bottom right": " "}
    current_player ="X"
    result = False
    while not result:
        display_board(current_positions)
        current_positions,current_player = user_move(current_positions,current_player)
        result= is_game_over(current_positions)
        if result:
            print "GAME OVER"
            print "Result: " + result
play_game()
