# Python libraries
import argparse
import time

# Own files
import timer
from timer import Timer

def largerThan(min):
    class Minimum(argparse.Action):
        def __call__(self, parser, args, value, option_string=None):
            if not min<value:
                msg = f"argument \"{self.dest}\" requires values larger than {min}"
                raise argparse.ArgumentTypeError(msg)
            setattr(args, self.dest, value)
    return Minimum

parser = argparse.ArgumentParser(description="Cmd line pomodoro timer")
parser.add_argument("duration", type=int, action=largerThan(0), help="the duration of the work session")
parser.add_argument("-c", "--continuous", action="store_true", help="the timer will continue running with breaks inbetween work sessions. The default break value is 5 min.")
parser.add_argument("-p", "--pause", type=int, choices=[10,15,20], help="Specifies length of the pauses", default=5)
args = parser.parse_args()

duration = args.duration * 60
pause = args.pause * 60

def countdown(s):
    """

    https://stackoverflow.com/questions/25189554/countdown-clock-0105
    """
    
    while s:
        _, mins, secs = timer.format_seconds(s)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        s -= 1

if args.continuous:
    while(True):
        t = Timer()
        t.start()
        countdown(duration)
        t.end()
        countdown(pause)
else:
    countdown(duration)

# t0 = countdown(duration)