import jdatetime


def to_jalali(time):
    start_time = jdatetime.datetime.fromgregorian(datetime=time, locale='fa_IR')
    start_time = start_time.strftime("%Y %m %d")
    return str(start_time)
