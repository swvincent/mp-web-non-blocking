import usocket
from uselect import select
from machine import Pin, PWM

html = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
    <head> <title>ESP8266 HTTP Test</title> </head>
    <body>
        <h1>It verks!</h1>
    </body>
</html>
"""


def toggle_led():
    led.value(not led.value())


def client_handler(client):
    # Whatever
    response = html

    client.send(response)
    client.close()


led = Pin(2, Pin.OUT)

addr = usocket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = usocket.socket()
# s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    r, w, err = select((s,), (), (), 1)
    if r:
        for readable in r:
            cl, addr = s.accept()
            try:
                client_handler(cl)
            except OSError as e:
                pass

    toggle_led()
