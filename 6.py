import jdatetime


def jalali_age(birth):
    thisyear = jdatetime.datetime.now().year
    age = thisyear - birth
    # print(age)
    return age

print(jalali_age(1370))
