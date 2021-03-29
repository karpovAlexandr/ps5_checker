import sys
from datetime import datetime
from time import sleep

from core.SearchEngine import SearchEngine


def waiting_please(timer):
    animation_speed = 0.1
    animation = "|/-\\"
    for i in range(int(timer // animation_speed)):
        sleep(animation_speed)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


# TODO make logger (on/off)
if __name__ == '__main__':
    while True:
        print(datetime.strftime(datetime.now(), "%d.%m %H:%M"))

        ps5 = SearchEngine(
            telegram=True,
            tests_on=True,
            sleep=60
        )
        ps5.run()
        waiting_please(ps5.sleep)
        print('\n\n')
