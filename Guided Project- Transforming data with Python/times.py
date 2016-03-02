import read
from dateutil.parser import parse

df = read.load_data()

times = df.submission_time

def hour_extract(datetimeobj):
    datetime_obj = parse(datetimeobj)
    return datetime_obj.hour

def day_extract(datetimeobj):
    return parse(datetimeobj).day

    
df['submission_hour'] = times.apply(lambda x: hour_extract(x))
sub_hour = df.submission_hour
sub_hour_counts = sub_hour.value_counts()

df['submission_day'] = times.apply(lambda x: day_extract(x))
sub_day = df.submission_day
sub_day_counts = sub_day.value_counts()

print(sub_day_counts[:8])