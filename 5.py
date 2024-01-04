from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz

shamsi = JalaliDateTime(1402, 10, 11, 0, 0, 0, 0, pytz.utc).strftime("%A")
print(shamsi)
