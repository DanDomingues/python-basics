#Ex 5.1
def double_number(number:int):
    return number * 2

#Ex 5.2
def get_written_out_datetime(date:str):
    year, month, day = date.split("/")
    month_index = int(month) - 1
    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )

    return f"{day} of {months[month_index]} of {year}"

#Ex 5.3
def get_max_number(*args):
    return max(args)

#Runtime
print(double_number(4))
print(get_max_number(4, 5, 12))
print(get_written_out_datetime("2025/03/16"))