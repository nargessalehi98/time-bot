from rubika_bot.models import Keypad, KeypadRow, Button, ButtonSelection, ButtonCalendar, ButtonNumberPicker, \
    ButtonStringPicker

Buttons = list()

start_button_time = Button(id='1', type='Simple', button_text='زمان فعلی')
start_button_cast = Button(id='1', type='Simple', button_text='تبدیل زمان')
Buttons.append(start_button_time)
Buttons.append(start_button_cast)
start_keypad = KeypadRow(buttons=[start_button_cast, start_button_time])
start_bot_keypad = Keypad(rows=start_keypad, resize_keypad=True, one_time_keypad=True)


stop_button_time = Button(id='1', type='Simple', button_text='شروع مجدد')
Buttons.append(stop_button_time)
stop_keypad = KeypadRow(buttons=[start_button_cast, start_button_time])
stop_bot_keypad = Keypad(rows=start_keypad, resize_keypad=True, one_time_keypad=True)

