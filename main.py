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


def scroll_down(mouse):
    mouse.scroll(0, 4 * random.randint(1, 4))


def scroll_up(mouse):
    mouse.scroll(0, -4 * random.randint(1, 4))


def loop(mouse, speed_coeficient, scroll):
    interval = random.randint(3, 10) / speed_coeficient
    click(mouse)
    time.sleep(interval)

    if scroll:
        if random.randint(0, 10) == 7:
            scroll_down(mouse)
        elif random.randint(0, 10) == 4:
            scroll_up(mouse)


def main():
    if(len(sys.argv) == 1):
        speed_coeficient = 4
    elif (len(sys.argv) == 2):
        speed_coeficient = int(sys.argv[1])
        scroll = False    
    else:
        speed_coeficient = int(sys.argv[1])
        scroll = bool(sys.argv[2])
    print('[ARGS]', 'speed_coeficient = ', speed_coeficient, '; scroll =', scroll)
    mouse = Controller()
    while True:
        loop(mouse, speed_coeficient, scroll)

if __name__ == "__main__":
    main()
