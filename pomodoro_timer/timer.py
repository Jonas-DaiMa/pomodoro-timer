import time
from datetime import timedelta, datetime

class Timer(object):

    _duration = timedelta(seconds=0)

    def start(self):
        self.initial = datetime.now()
        self._started = True
        return True

    def pause(self):
        if self._started:
            self._duration += datetime.now() - self.initial
            self._started = False
            return True
        else:
            return self._started

    def end(self):
        if self._started:
            self._duration += datetime.now() - self.initial
            self._started = False
            return True
        else:
            return False

    def get_duration(self):
        return self._duration

    def reset(self):
        self._duration = timedelta(seconds=0)
        self._started = False

    def __str__(self):
        hours, mins, secs = format_timer(self)
        return f"{hours:02d}:{mins:02d}:{secs:02d}"

def format_seconds(seconds):
    secs = int(seconds)
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return h,m,s

def format_timer(t : Timer):
    return format_seconds(t._duration.total_seconds())

def format_minutes(minutes):
    return format_seconds(minutes*60)


# timer = Timer()

# print ( timer.start() )
# time.sleep(1)
# print( timer.pause() )
# time.sleep(1)
# print ( timer.end() )
# time.sleep(1)
# print ( timer.start() )
# time.sleep(1)
# print ( timer.end() )
# print()
# print( format(timer) )