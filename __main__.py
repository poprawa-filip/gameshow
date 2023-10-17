import buzz
from player import Player

def main():
    print("Welcome to Buzz!")
    print("Input the names of the players.")

    players = []

    player = input("Player's one name\n")
    contestant = Player(player, 1)
    players.append(contestant)

    
    player = input("Player's two name\n")
    contestant = Player(player, 2)
    players.append(contestant)

    player = input("Player's three name\n")
    contestant = Player("Charlie", 3)
    players.append(contestant)

    print("Behold, our contestants!")
    print("-----------------------------------------------------")
    for player in players:
        player.display_player()
        print("-----------------------------------------------------")

    print("Now, let's pair the buzzers!")

    buzz_system = buzz.check_for_buzz_dongle()
    answer = input("Do you want to pair the buzzers? Input N to skip.\n")
    if (answer != "N"):
        buzz.pair_buzzers(buzz_system)

    input("Buzzers are paired, let's go! Hit enter to continue")

    while(True):
        first_player_index = buzz.input_loop_until_first_player(buzz_system)
        print("-----------------------------------------------------")
        print(players[first_player_index-1].player_name, "buzzed first!")
        print("-----------------------------------------------------")
        input("Hit enter to restart input loop.")

if __name__ == '__main__':
    main()