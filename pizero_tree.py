from machine import Pin, PWM
import utime

leds = [PWM(Pin(i), freq=1000) for i in range(2, 28)]

led_value = 0
led_speed = 5

while True:
    for led in leds:
        led_value += led_speed
        led.duty_u16(int(led_value * 500))
        utime.sleep_ms(100)
    utime.sleep_ms(200)
    if led_value >= 100:
        led_value = 100
        led_speed = -5
    if led_value <= 0:
        led_value = 0
        led_speed = 5
