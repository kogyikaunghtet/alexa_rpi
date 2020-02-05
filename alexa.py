import fauxmo
import logging
import time
import sys
import RPi.GPIO as GPIO
from debounce_handler import debounce_handler
GPIO.setmode(GPIO.BOARD)
GPIO.setup(int(11), GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(int(12), GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(int(13), GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(int(15), GPIO.OUT, initial=GPIO.LOW)
logging.basicConfig(level=logging.DEBUG)

class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    TRIGGERS = {"yellow light": 52000, "green light": 51000, "red light": 53000, "blue light": 52002}
    def act(self, client_address, state, name):
        print("State", state, "from client @", client_address)
        if name=="yellow light":
            GPIO.output(int(11), state)
        elif name =="green light":
            GPIO.output(int(12), state)
        elif name =="red light":
            GPIO.output(int(13), state)
        elif name == "blue light":
            GPIO.output(int(15), state)
        return True

if __name__ == "__main__":
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)

    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            p.poll(100)
            time.sleep(0.1)
        except Exception as e:
            logging.critical("Critical exception: "+ e.args  )
            break
