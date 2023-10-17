import hid
import _thread

# constants

buzz_vendor_id = 1356
buzz_product_id = 4096
buzz_init_message = b"\x00"*5

# player 1 codes

player_one_buzz_in = b'\x00\x00\x01\x00\xf0'
player_one_led = b'\x00\x00\xff\x00\xf0'

# player 2 codes

player_two_buzz_in = b'\x00\x00\x20\x00\xf0'
player_two_led = b'\x00\x00\x00\xff\xf0'

# player 3 codes

player_three_buzz_in = b'\x00\x00\x00\x04\xf0'
player_three_led = b'\x00\x00\x00\x00\xff'

leds_off = b'\x00\x00\x00\x00\x00'

def input_thread(loop_list):
    input()
    loop_list.append(True)

def check_for_buzz_dongle():
    buzz_receiver = None
    print("Connect wireless Buzz! dongle to proceed. If it is connected, wait a moment.")
    while buzz_receiver is None: 
        try:
            buzz_receiver = hid.Device(buzz_vendor_id, buzz_product_id)
        except hid.HIDException:
            pass
    print("Buzz receiver dongle is present.")
    return buzz_receiver

def pair_buzzers(buzz_receiver):
    print("Follow these steps:")
    print("1.Turn on all needed buzzers.")
    print("2.Put them into pairing mode.")
    print("3. Hold a bind button on a receiver until Buzzers blink.")
    print("Once done, hit enter to write zeroes to the receiver.")

    loop_list=[]
    _thread.start_new_thread(input_thread, (loop_list,))
    while not loop_list:
        pass

    print("Writing data to the dongle...")
    buzz_receiver.write(buzz_init_message)
    print("Write complete. Check whether controllers react with the receiver.")
    print("If not, press the bind button on receiver again, until buzzer blinks,")
    print("BUT ONLY for short time!")

def listen_for_buzz_in(buzz_receiver):
    return buzz_receiver.read(6)

def discard_leftover_input(buzz_receiver):
    while buzz_receiver.read(6, timeout=250):
        pass

def led_on(buzz_receiver, player_number):
    if (player_number == 1):
        buzz_receiver.write(player_one_led)
    elif (player_number == 2):
        buzz_receiver.write(player_two_led)
    elif (player_number == 3):
        buzz_receiver.write(player_three_led)

def get_first_buzz(buzz_receiver, response):
    if (response == player_one_buzz_in):
        return 1
    elif (response == player_two_buzz_in):
        return 2
    elif (response == player_three_buzz_in):
        return 3
    else:
        return 0

def led_off(buzz_receiver):
    buzz_receiver.write(leds_off)

def input_loop_until_first_player(buzz_receiver):
    led_off(buzz_receiver)
    discard_leftover_input(buzz_receiver)
    print("Waiting for a player to buzz in...")
    response = listen_for_buzz_in(buzz_receiver)
    first_player = get_first_buzz(buzz_receiver, response)
    while (first_player == 0):
        response = listen_for_buzz_in(buzz_receiver)
        first_player = get_first_buzz(buzz_receiver, response)
    
    led_on(buzz_receiver, first_player)
    
    return first_player




