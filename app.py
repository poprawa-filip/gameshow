import hid
import _thread

def input_thread(loop_list):
    input()
    loop_list.append(True)

# constants

buzz_vendor_id = 1356
buzz_product_id = 4096
buzz_init_message = b"0"*6
buzzers_led_off = b"0"*5

# player 1 codes

player_one_buzz_in = b"0"*2 + [b"1"]
player_one_led_on = [b"0"] + [b"FF"]

# player 2 codes

player_two_buzz_in = b"0"*2 + [b"2"]
player_two_led_on = [b"0"]*2 + [b"FF"]

# player 3 codes

player_three_buzz_in = b"0"*3 + [b"4"]
player_three_led_on = [b"0"]*3 + [b"FF"]

buzz_receiver = None
print("Connect wireless Buzz! dongle to proceed.")
while buzz_receiver is None: 
    try:
        buzz_receiver = hid.Device(buzz_vendor_id, buzz_product_id)
    except hid.HIDException:
        pass
print("Buzz receiver dongle is present.")

print("Follow these steps:")
print("1.Turn on all needed buzzers.")
print("2.Put them into pairing mode.")
print("3. Hold a bind button on a receiver until Buzzers blink.")
print("Once done, press any key to write zeroes to the receiver.")

loop_list=[]
_thread.start_new_thread(input_thread, (loop_list,))
while not loop_list:
    pass

print("Writing data to the dongle...")
buzz_receiver.write(buzz_init_message)
print("Write complete. Check whether controllers react with the receiver.\
      If not, press the bind button on receiver again, until buzzer blinks,\
      but only for short time! ")

