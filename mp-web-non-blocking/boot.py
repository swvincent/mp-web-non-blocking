"""
This file is executed on every boot (including wake-boot from deepsleep)
"""

import network

def no_debug():
    import esp
    esp.osdebug(None)


def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ssid', 'password')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def disable_ap():
    # Disable Access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)


import gc
gc.collect()

# no_debug()
disable_ap()
connect_wifi()