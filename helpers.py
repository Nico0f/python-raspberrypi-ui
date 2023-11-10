def format_date(day):
    day_string_array = str(day).split('-')
    return [int(x) for x in day_string_array]

def create_month_array(month_iter, i = 0, arr = [], iter_number = 1):
    length = len(month_iter)
    if i+1 == length:
        return arr
    sub_array = []
    while (i%(7*iter_number) != 0 or i == 0) and i < length:
        sub_array.append(month_iter[i])
        i += 1
    else:
        if i != length:
            arr.append(sub_array)
            return create_month_array(month_iter, i, arr, iter_number+1)
        else:
            arr.append(sub_array)
            return arr
        
def generate_calendar(month_subarrays, current_month):
    calendar_body = ''
    for sub_array in month_subarrays:
        validity = check_valid_month(sub_array, current_month)
        if validity:
            for day_selected in sub_array:
                [_, month, day] = format_date(day_selected)
                if month == current_month:
                     calendar_body = calendar_body + f'<a href="" class="div-cell">{day}</a>'
                else:
                     calendar_body = calendar_body + f'<a href="" class="div-cell-inactive">{day}</a>'
    return calendar_body

def check_valid_month(sub_array, current_month):
    validity = False
    for day in sub_array:
        [_, month, _] = format_date(day)
        if month == current_month:
            validity = True
    return validity