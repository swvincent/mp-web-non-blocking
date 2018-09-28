# mp-web-non-blocking

Very basic example of a non-blocking web server running on MicroPython. Written for ESP8266-based boards such as NodeMCU, may work on others?

This program serves a very simple webpage on port 80, and toggles the built-in LED. The LED changes every second which is the length of the timeout for the socket serving the web page.

It's based on an [example I found online](https://forum.micropython.org/viewtopic.php?t=4211). I don't claim to fully understand it, but I did get it working. It didn't meet my needs though due to the long timeout, so I didn't do anything further with it. I've shared it in hopes it may be of value to someone else.

To use it, you'll need to specify your WiFi settings in boot.py.