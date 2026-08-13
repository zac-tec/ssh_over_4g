from gpiozero import DigitalOutputDevice
import atexit

RELAY_PIN = 17

# create relay ONLY once with safe default OFF
relay = DigitalOutputDevice(RELAY_PIN, initial_value=True)


def relay_on():
    relay.off()      # ACTIVE LOW → ON
    print("Relay ON")


def relay_off():
    relay.on()       # HIGH → OFF
    print("Relay OFF")


def cleanup():
    relay.on()
    relay.close()
    print("Relay cleaned up")

atexit.register(cleanup)
