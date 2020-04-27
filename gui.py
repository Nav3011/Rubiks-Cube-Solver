import tkinter as tk
import tkinter.font as tkFont
input_state = list()
def Cube_String(string):
    for i in range(len(string)):
        i=i+1
    return string
notation = ['U', 'L', 'F', 'R', 'B', 'D']
def update_notation():
    global input_state
    global count
    count = count + 1
    pos = ['U', 'L', 'F', 'R', 'B', 'D']
    pos[0] = up.get()
    pos[1] = left.get()
    pos[2] = front.get()
    pos[3] = right.get()
    pos[4] = back.get()
    pos[5] = down.get()
    for i in range(6):
        if pos[i] != '':
            if pos[i] not in input_state:
                input_state.append(pos[i])
    # input_state.append()

root = tk.Tk()

root.state('zoomed')
fontStyle = tkFont.Font(family="Lucida Grande", size=14)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
messages = list()
messages.append("Loading the GUI...")

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=4)
root.rowconfigure(2, weight=4)
root.rowconfigure(3, weight=1)

title = tk.Frame(root,bg="green")
title.grid(column=0, row=0, columnspan=2, sticky="NSEW")

canvas = tk.Canvas(root, bg="white")
canvas.grid(column=0, row=1, rowspan=2, sticky="NSEW")
canvas.grid_propagate(0)

state = tk.Frame(root, bg="white")
state.grid(column=1, row=1, sticky="NSEW")
state.grid_propagate(0)
# cube_state = ''
control = tk.Frame(root, bg="white")
control.grid(column=1, row=2, sticky="NSEW")
control.grid_propagate(0)

console = tk.Frame(root, bg="white")
console.grid(column=0, row=3, columnspan=2 ,sticky="NSEW")
console.grid_propagate(0)
# draw_grid(canvas)
canvas.update()
canvas_width = canvas.winfo_width()
canvas_height = canvas.winfo_height()
# print(canvas_width, canvas_height)
cell_size = 48
cell_pad = 7
face_pad = 18
face_width = 3*cell_size+2*cell_pad

x = 4*face_width + 3*face_pad
A = round((canvas_width - x ) / 2)
y = 3*face_width + 2*face_pad
B = round((canvas_height - y ) / 2)
new_origin = (A, B)
cubie_ids = list()
# start_points=[U,R,F,D,L,B,]
start_points = [(new_origin[0]+face_width+face_pad,new_origin[1]),
                (new_origin[0]+2*face_width+2*face_pad,new_origin[1]+face_width+face_pad),
                (new_origin[0]+face_width+face_pad,new_origin[1]+face_width+face_pad),
                (new_origin[0]+face_width+face_pad,new_origin[1]+2*face_width+2*face_pad),
                (new_origin[0],new_origin[1]+face_width+face_pad),
                (new_origin[0]+3*face_width+3*face_pad,new_origin[1]+face_width+face_pad),
                ]
# print(start_points)
for i in start_points:
    for j in range(3):
        for k in range(3):
            x_coor = i[0]+(cell_size+cell_pad)*k
            y_coor = i[1]+(cell_size+cell_pad)*j
            w = canvas.create_rectangle(x_coor, y_coor, x_coor+cell_size, y_coor+cell_size, outline="#000")
            # print(canvas.coords(w))
            # print(w)
            cubie_ids.append(w)

# show_message('Grid Generated')
# state_input(state)
state.columnconfigure(0, weight=1)
state.columnconfigure(1, weight=2)
for i in range(6): 
    state.rowconfigure(i, weight=1)
tk.Label(state, text="Up", bg="white", font = fontStyle).grid(row=0, sticky="NSEW")
tk.Label(state, text="Left",bg="white", font = fontStyle).grid(row=1, sticky="NSEW")
tk.Label(state, text="Front",bg="white", font = fontStyle).grid(row=2, sticky="NSEW")
tk.Label(state, text="Right",bg="white", font = fontStyle).grid(row=3, sticky="NSEW")
tk.Label(state, text="Back",bg="white", font = fontStyle).grid(row=4, sticky="NSEW")
tk.Label(state, text="Down",bg="white", font = fontStyle).grid(row=5, sticky="NSEW")

up = tk.Entry(state, font = fontStyle)
left = tk.Entry(state, font = fontStyle)
front = tk.Entry(state, font = fontStyle)
right = tk.Entry(state, font = fontStyle)
back = tk.Entry(state, font = fontStyle)
down = tk.Entry(state, font = fontStyle)

up.grid(row=0, column=1)
left.grid(row=1, column=1)
front.grid(row=2, column=1)
right.grid(row=3, column=1)
back.grid(row=4, column=1)
down.grid(row=5, column=1)

# Control(control)
control.rowconfigure(0, weight=1)
control.rowconfigure(1, weight=1)
control.rowconfigure(2, weight=1)
control.columnconfigure(0, weight=1)
control.columnconfigure(1, weight=1)

send_gui = tk.Button(control, font=fontStyle, text="Send to GUI", command=update_notation, width=10)
solve = tk.Button(control, font=fontStyle, text="Solve", width=10)
reset = tk.Button(control, font=fontStyle, text="Reset", width=10)
nxt = tk.Button(control, font=fontStyle, text="Next", width=10)
animate = tk.Button(control, font=fontStyle, text="Animate", width=10)
send_arduino = tk.Button(control, font=fontStyle, text="Send to Arduino", width=10)

send_gui.grid(row=0, column=0)
solve.grid(row=0, column=1)
reset.grid(row=2, column=1)
nxt.grid(row=1, column=1)
animate.grid(row=1, column=0)
send_arduino.grid(row=2, column=0)

# display_console(console)
console.rowconfigure(0, weight=1)
console.columnconfigure(0, weight=1)
message = tk.Label(console, bg="black", fg="white", font=fontStyle)
message.grid(row=0, column=0, sticky="NSEW")
root.mainloop()