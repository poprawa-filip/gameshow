import buzz

class Player:
    def __init__(self, name, player_number):
        self.player_name = name
        self.player_number = player_number
        if (player_number == 1):
            self.buzz_in_code = buzz.player_one_buzz_in
            self.led_code = buzz.player_one_led
        elif (player_number == 2):
            self.buzz_in_code = buzz.player_two_buzz_in
            self.led_code = buzz.player_two_led
        elif (player_number == 3):
            self.buzz_in_code = buzz.player_three_buzz_in
            self.led_code = buzz.player_three_led
        else:
            self.buzz_in_code = None
            self.led_code = None
            print("Buzz in and LED codes for player are not initialized.")
            print("Check and restart the program, because this shouldn't be possible.")
        
    def display_player(self):
        print("Name:", self.player_name)
        print("Player number:", self.player_number)
        print("Player's Buzz! code:", self.buzz_in_code)
        print("Player's LED code:", self.led_code)