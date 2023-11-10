# import requests

# url = 'https://api.tomorrow.io/v4/timelines?location=-34.61632573295411, -58.92236094576923&fields=temperature&timesteps=1h&units=metric&apikey=C9zkMvne7FJEiBZbvNzQLd5SrMn4FOnB&fields=precipitationProbability'
# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)
# print(response.headers)
# html = '<!DOCTYPE html><html><head><title>My Minimal Web Page</title><style>.main-body {height: 100vh; /* Optional: Set the height of the grid to fill the viewport */}.calendar-body {display: grid;grid-template-columns: repeat(7, 1fr);grid-template-rows: repeat(6, 1fr);gap: 5px; /* Optional: Adds some spacing between grid items */height: 100%;}.day-body {display: grid;grid-template-columns: repeat(7, 1fr);gap: 5px; /* Optional: Adds some spacing between grid items */text-align: center;font-size: 22px;}.day-cell {background-color: black;color: white;margin-bottom: 5px;}/* Optional: Add some styling to the grid items */.div-cell {background-color: #f0f0f0;padding: 10px;text-align: center;font-size: 20px;text-align: end;}</style></head><body class="main-body"><div style="height: 200px;">UPPER PART</div><div class="day-body"><span class="day-cell">Domingo</span><span class="day-cell">Lunes</span><span class="day-cell">Martes</span><span class="day-cell">Miércoles</span><span class="day-cell">Jueves</span><span class="day-cell">Viernes</span><span class="day-cell">Sábado</span></div><div class="calendar-body">{calendar_body}</body></html>'



import calendar
import datetime
from helpers import format_date, create_month_array, generate_calendar

def main():
    today = datetime.date.today()
    [current_year, current_month, current_day] = format_date(today)

    month_days = calendar.Calendar(firstweekday=6).itermonthdates(current_year,current_month)
    month_days_string_array = [str(x) for x in month_days]

    month_subarrays = create_month_array(month_days_string_array)

    calendar_body = generate_calendar(month_subarrays, current_month)

    # html = '<!DOCTYPE html><html><head><title>My Minimal Web Page</title><style>.main-body {@font-face {font-family: \'Geist\';src: url(\'./Geist/Geist-Regular.woff2\') format(\'woff2\'), /* Add each font variant */url(\'./Geist/Geist-Bold.woff2\') format(\'woff2\'),url(\'./Geist/Geist-Light.woff2\') format(\'woff2\');font-weight: normal; /* You may specify the font-weight if needed */font-style: normal; /* You may specify the font-style if needed */}font-family: \'Geist\', sans-serif;height: 100vh; /* Optional: Set the height of the grid to fill the viewport */}.calendar-body {display: grid;grid-template-columns: repeat(7, 1fr);grid-template-rows: repeat(6, 1fr);gap: 1px; /* Optional: Adds some spacing between grid items */background-color: gray;padding: 0px 1px 0px 1px;height: 100%;}.day-body {display: grid;grid-template-columns: repeat(7, 1fr);gap: 5px; /* Optional: Adds some spacing between grid items */text-align: center;font-size: 22px;}.day-cell {background-color: black;color: white;margin-bottom: 5px;} /* Optional: Add some styling to the grid items */.div-cell {background-color: #f0f0f0;padding: 10px;text-decoration: none;color: black;text-align: center;font-size: 17px;text-align: end;}.div-cell-inactive {background-color: #686868;padding: 10px;text-decoration: none;color: black;text-align: center;font-size: 17px;text-align: end;}</style></head><body class="main-body"><div style="height: 200px">UPPER PART</div><div class="day-body"><span class="day-cell">Domingo</span><span class="day-cell">Lunes</span><span class="day-cell">Martes</span><span class="day-cell">Miércoles</span><span class="day-cell">Jueves</span><span class="day-cell">Viernes</span><span class="day-cell">Sábado</span></div><div class="calendar-body">calendar_body</div></body></html>'
   
    html_import = open('template.html', 'r')
    template = html_import.read()
    html_import.close()

    new_html = template.replace('calendar_body', calendar_body).replace("'", "\'").replace('rows_to_change', str(len(month_subarrays)))

    f = open('test.html', 'w')
    file = f.write(new_html)
    f.close()

main()

