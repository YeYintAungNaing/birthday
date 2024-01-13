from datetime import datetime, date
import inflect
import sys

#current_time = datetime.now()
current_time = datetime.today()

print(current_time)


birthday = input('enter your birthday [y-m-d]: ')

try:
    birthday_ = datetime.strptime(birthday, "%Y-%m-%d")
    print(birthday)
       
except ValueError:
    print('Invaild')
    sys.exit()
    

time_difference = current_time - birthday_


diff_in_min = int(time_difference.total_seconds() / 60)
p = inflect.engine()
words = p.number_to_words(diff_in_min) # type: ignore

print(f"{words} minutes")

