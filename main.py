from pynput.mouse import Button, Controller
import time
import random
import sys

def test(mouse):
    # Read pointer position
    print('The current pointer position is {0}'.format(
        mouse.position))

    # Set pointer position
    mouse.position = (10, 20)
    print('Now we have moved it to {0}'.format(
        mouse.position))

    # Move pointer relative to current position
    mouse.move(5, -5)

    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    # Double click; this is different from pressing and releasing
    # twice on Mac OSX
    mouse.click(Button.left, 2)

    # Scroll two steps down
    mouse.scroll(0, 2)

def click(mouse):
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

def loop(mouse, speed_coeficient):
    interval = random.randint(3, 10) / speed_coeficient
    click(mouse)
    time.sleep(interval)

def main():
    if(len(sys.argv) == 1):
        speed_coeficient = 4
    else:
        speed_coeficient = sys.argv[1]
    print('[ARGS]', 'speed_coeficient = ', speed_coeficient)
    mouse = Controller()
    while True:
        loop(mouse, speed_coeficient)

if __name__ == "__main__":
    main()
