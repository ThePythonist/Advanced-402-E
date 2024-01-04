import jdatetime

# now = str(jdatetime.datetime.now()).split()
# date = now[0]
# time = now[1]
# thisyear = date.split("-")[0]
# print(thisyear)

# -----------------------------------------------------

# year = jdatetime.datetime.now().year
# print(year)

# -----------------------------------------------------

year = jdatetime.datetime.now()
print(year.strftime("%Y"))
