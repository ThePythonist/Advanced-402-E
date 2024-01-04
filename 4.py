import jdatetime

# now = str(jdatetime.datetime.now()).split()
# date = now[0].split("-")
# month = date[1]
# day = date[2]
#
# print(month)
# print(day)

# -----------------------------------------------------

# month = jdatetime.datetime.now().month
# day = jdatetime.datetime.now().day
# print(f"{month}/{day}")

# -----------------------------------------------------

now = jdatetime.datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
print(f"{month}/{day}")
