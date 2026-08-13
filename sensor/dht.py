import adafruit_dht
import board

dht_pin = board.D4

temperature = None
humidity = None


def read_sensor():
    global temperature, humidity

    try:
        dht = adafruit_dht.DHT11(dht_pin, use_pulseio=False)
        temperature = dht.temperature
        humidity = dht.humidity
        dht.exit()
    except RuntimeError:
        pass

    return temperature, humidity
