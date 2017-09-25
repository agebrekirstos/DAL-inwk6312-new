class Time(object):
    """class time hour:min:sec"""

time = Time()
time.hour = 10
time.minute = 51
time.second = 20

def print_time(t):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))
def is_after(t1,t2):
    t1 = Time()
    t2 = Time()
    return t2.hour > t1.hour or t2.minute > t1.minute or t2.second > t1.second


print_time(time)
