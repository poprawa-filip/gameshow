import hid
import _thread

def input_thread(loop_list):
    input()
    loop_list.append(True)

print ("Hi, mom")

buzz_vendor_id = 1356
buzz_product_id = 4096

buzz_receiver = None
print("Connect wireless Buzz! dongle to proceed.")
while buzz_receiver is None: 
    try:
        buzz_receiver = hid.Device(buzz_vendor_id, buzz_product_id)
    except hid.HIDException:
        pass
print(buzz_receiver.product)
print("Follow these steps:")
print("1.Turn on all needed buzzers.")
print("2.Put them into pairing mode.")
print("3. Hold a bind button on a receiver until Buzzers blink.")
print("Once done, press any key to write data to the receiver.")

loop_list=[]
_thread.start_new_thread(input_thread, (loop_list,))
while not loop_list:
    pass

