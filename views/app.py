from tkinter import *
from commons import Color
from time import strftime

# variables
min = None
sec = None

# funcs
def time():
    str_time = strftime('%M:%S %p')
    label_clock.config(text=str_time)
    label_clock.after(1000, time)


def format_time(min, sec):
    format_min = ['0', '0']
    format_sec = ['0', '0']

    if min < 10:
        format_min[1] = str(min)
    else:
        format_min = str(min).split()
    if sec < 10:
        format_sec[1] = str(sec)
    else:
        format_sec = str(sec).split()
    return '{min}:{sec}'.format(min=''.join(format_min), sec=''.join(format_sec))


def initial_state():
    global min, sec
    min, sec = None, None
    label_clock.config(text='00:00', fg=Color.sucess, font=("Arial", 40))


def tick():
    global min
    global sec
    if sec == None and min == None:
        min = 0
        sec = 0
    if sec == 5:
        label_clock.config(text='Fim do pomodoro!', fg=Color.danger, font=("Arial", 40))
        label_log_text.config(text='1º Pomodoro = Sucefull')
        label_clock.after(2000, initial_state)
    else:
        sec += 1
        if sec == 60:
            min += 1
            sec = 0
        label_clock.config(text=format_time(min, sec))
        label_clock.after(1000, tick)


window = Tk()

# windows style
window.title('Pymodoro')
window["bg"] = Color.light
window.resizable(False, False)
window.geometry("700x450+100+100")


# clock container
clock_container = Frame(window, width=500, height=450, background=Color.dark)
clock_container.pack(side=LEFT)
clock_container.pack_propagate(False)

# clock label
label_clock = Label(
    clock_container,
    text="00:00",
    bg=Color.dark,
    fg=Color.sucess,
    font=("Arial", 40),
    anchor=CENTER
)
label_clock.pack(side=TOP, padx=10, pady=10)

# log container
log_container = Frame(window, width=200, height=450, background=Color.light)
log_container.pack(side=RIGHT)
log_container.pack_propagate(False)

#log label
label_log = Label(
    log_container,
    text="Logs",
    bg=Color.light,
    fg=Color.warning,
    font=("Arial", 25),
    anchor=CENTER
)
label_log.pack(side=TOP, padx=10, pady=10)

#log label text
label_log_text = Label(
    log_container,
    text="1º Pomodoro = Working",
    bg=Color.light,
    fg=Color.warning,
    font=("Arial", 12),
    anchor=CENTER
)
label_log_text.pack(side=TOP, padx=10, pady=10)

# controls container
controls_container = Frame(clock_container, width=500, height=100, background=Color.dark)
controls_container.pack(side=BOTTOM)
controls_container.pack_propagate(False)

# start button
start_button = Button(
    controls_container,
    width=20,
    height=2,
    bg=Color.warning,
    fg=Color.dark,
    text="Start",
    font=("Arial", 10),
    command=tick
)
start_button.pack(side=LEFT, padx=10, pady=20)

# pause button
pause_button = Button(
    controls_container,
    width=20,
    height=2,
    bg=Color.warning,
    fg=Color.dark,
    text="Pause",
    font=("Arial", 10)
)
pause_button.pack(side=RIGHT, padx=10, pady=20)


window.mainloop()