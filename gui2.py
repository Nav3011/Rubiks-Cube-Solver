import tkinter as tk
import tkinter.font as tkFont
import kociemba

class Cubie:
	def __init__(self, master):
		self.master = master
		self.fontStyle = tkFont.Font(family="Lucida Grande", size=14)
		self.master.state('zoomed')
		self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
		self.cell_size = 48
		self.cell_pad = 7
		self.face_pad = 18
		self.face_width = 3*self.cell_size+2*self.cell_pad
		self.count=0
		self.input_state=list()
		self.cubie_color = ['']*54
		self.cube_string=''
		self.layout()
		self.draw_grid()
	def layout(self):
		self.master.columnconfigure(0, weight=2)
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(0, weight=1)
		self.master.rowconfigure(1, weight=4)
		self.master.rowconfigure(2, weight=4)
		self.master.rowconfigure(3, weight=1)
		self.title = tk.Frame(root,bg="green")
		self.title.grid(column=0, row=0, columnspan=2, sticky="NSEW")
		self.canvas = tk.Canvas(root, bg="white")
		self.canvas.grid(column=0, row=1, rowspan=2, sticky="NSEW")
		self.canvas.grid_propagate(0)
		self.state = tk.Frame(root, bg="white")
		self.state.grid(column=1, row=1, sticky="NSEW")
		self.state.grid_propagate(0)
		self.control = tk.Frame(root, bg="white")
		self.control.grid(column=1, row=2, sticky="NSEW")
		self.control.grid_propagate(0)
		self.console = tk.Frame(root, bg="white")
		self.console.grid(column=0, row=3, columnspan=2 ,sticky="NSEW")
		self.console.grid_propagate(0)
		self.canvas.update()
		self.canvas_width = self.canvas.winfo_width()
		self.canvas_height = self.canvas.winfo_height()
		self.state.columnconfigure(0, weight=1)
		self.state.columnconfigure(1, weight=2)
		for i in range(6):
			self.state.rowconfigure(i, weight=1)
		tk.Label(self.state, text="Up", bg="white", font = self.fontStyle).grid(row=0, sticky="NSEW")
		tk.Label(self.state, text="Right",bg="white", font = self.fontStyle).grid(row=1, sticky="NSEW")
		tk.Label(self.state, text="Front",bg="white", font = self.fontStyle).grid(row=2, sticky="NSEW")
		tk.Label(self.state, text="Down",bg="white", font = self.fontStyle).grid(row=3, sticky="NSEW")
		tk.Label(self.state, text="Left",bg="white", font = self.fontStyle).grid(row=4, sticky="NSEW")
		tk.Label(self.state, text="Back",bg="white", font = self.fontStyle).grid(row=5, sticky="NSEW")
		self.up = tk.Entry(self.state, font = self.fontStyle)
		self.right = tk.Entry(self.state, font = self.fontStyle)
		self.front = tk.Entry(self.state, font = self.fontStyle)
		self.down = tk.Entry(self.state, font = self.fontStyle)
		self.left = tk.Entry(self.state, font = self.fontStyle)
		self.back = tk.Entry(self.state, font = self.fontStyle)
		self.up.grid(row=0, column=1)
		self.right.grid(row=1, column=1)
		self.front.grid(row=2, column=1)
		self.down.grid(row=3, column=1)
		self.left.grid(row=4, column=1)
		self.back.grid(row=5, column=1)
		self.control.rowconfigure(0, weight=1)
		self.control.rowconfigure(1, weight=1)
		self.control.rowconfigure(2, weight=1)
		self.control.columnconfigure(0, weight=1)
		self.control.columnconfigure(1, weight=1)
		self.send_gui = tk.Button(self.control, font=self.fontStyle, text="Send to GUI", command=self.update, width=15)
		self.solve = tk.Button(self.control, font=self.fontStyle, text="Solve", command=self.solve, width=15)
		self.reset = tk.Button(self.control, font=self.fontStyle, text="Reset", command=self.reset, width=15)
		self.nxt = tk.Button(self.control, font=self.fontStyle, text="Next", width=15)
		self.animate = tk.Button(self.control, font=self.fontStyle, text="Animate",width=15)
		self.send_arduino = tk.Button(self.control, font=self.fontStyle, text="Send to Arduino", width=15)
		self.send_gui.grid(row=0, column=0)
		self.solve.grid(row=0, column=1)
		self.reset.grid(row=2, column=1)
		self.nxt.grid(row=1, column=1)
		self.animate.grid(row=1, column=0)
		self.send_arduino.grid(row=2, column=0)
		self.console.rowconfigure(0, weight=1)
		self.console.columnconfigure(0, weight=1)
		self.message = tk.Label(self.console, bg="black", fg="white", font=self.fontStyle)
		self.message.grid(row=0, column=0, sticky="NSEW")
	def draw_grid(self):
		self.x = 4*self.face_width + 3*self.face_pad
		self.A = round((self.canvas_width - self.x ) / 2)
		self.y = 3*self.face_width + 2*self.face_pad
		self.B = round((self.canvas_height - self.y ) / 2)
		self.new_origin = (self.A, self.B)
		self.cubie_ids = list()
		self.start_points = [(self.new_origin[0]+self.face_width+self.face_pad,self.new_origin[1]),(self.new_origin[0]+2*self.face_width+2*self.face_pad,self.new_origin[1]+self.face_width+self.face_pad),(self.new_origin[0]+self.face_width+self.face_pad,self.new_origin[1]+self.face_width+self.face_pad),(self.new_origin[0]+self.face_width+self.face_pad,self.new_origin[1]+2*self.face_width+2*self.face_pad),(self.new_origin[0],self.new_origin[1]+self.face_width+self.face_pad),(self.new_origin[0]+3*self.face_width+3*self.face_pad,self.new_origin[1]+self.face_width+self.face_pad)]
		for i in self.start_points:
			for j in range(3):
				for k in range(3):
					self.x_coor = i[0]+(self.cell_size+self.cell_pad)*k
					self.y_coor = i[1]+(self.cell_size+self.cell_pad)*j
					self.w = self.canvas.create_rectangle(self.x_coor, self.y_coor, self.x_coor+self.cell_size, self.y_coor+self.cell_size, outline="#000")
					self.cubie_ids.append(self.w)
		self.update_gui()
	def update(self):
		self.update_notation()
		if self.count == 5:
			self.convert_notation()	
		self.update_gui()
		self.count = self.count + 1
	def update_notation(self):
		self.pos = ['']*6
		self.pos[0] = self.up.get()
		self.pos[1] = self.right.get()
		self.pos[2] = self.front.get()
		self.pos[3] = self.down.get()
		self.pos[4] = self.left.get()
		self.pos[5] = self.back.get()
		for i in range(6):
			if self.pos[i] != '':
				if self.pos[i] not in self.input_state:
					self.input_state.append(self.pos[i])
		for i in range(len(self.input_state)):
			for j in range(len(self.input_state[i])):
				self.cubie_color[9*i+j]=self.input_state[i][j]
	def convert_notation(self):
		self.u = self.cubie_color[4]
		self.r = self.cubie_color[13]
		self.f = self.cubie_color[22]
		self.d = self.cubie_color[31]
		self.l = self.cubie_color[40]
		self.b = self.cubie_color[49]
		for i in self.cubie_color:
			if i == self.u:
				self.cube_string = self.cube_string + 'U'
			elif i == self.r:
				self.cube_string = self.cube_string + 'R'
			elif i == self.f:
				self.cube_string = self.cube_string + 'F'
			elif i == self.d:
				self.cube_string = self.cube_string + 'D'
			elif i == self.l:
				self.cube_string = self.cube_string + 'L'
			elif i == self.b:
				self.cube_string = self.cube_string + 'B'
		# print(self.cube_string)
	def solve(self):
		print(kociemba.solve(self.cube_string))
	def reset(self):
		self.count=0
		self.input_state=list()
		self.cubie_color = ['']*54
		self.cube_string=''
		self.pos = ['']*6
		self.up.delete(0, 'end')
		self.right.delete(0, 'end')
		self.front.delete(0, 'end')
		self.down.delete(0, 'end')
		self.left.delete(0, 'end')
		self.back.delete(0, 'end')
		self.update()
	def update_gui(self):
		for i in range(len(self.cubie_color)):
			if self.cubie_color[i] == '':
				self.canvas.itemconfig(self.cubie_ids[i], fill='gray93')
			elif self.cubie_color[i] == 'Y':
				self.canvas.itemconfig(self.cubie_ids[i], fill='yellow2')
			elif self.cubie_color[i] == 'B':
				self.canvas.itemconfig(self.cubie_ids[i], fill='RoyalBlue1')
			elif self.cubie_color[i] == 'R':
				self.canvas.itemconfig(self.cubie_ids[i], fill='firebrick1')
			elif self.cubie_color[i] == 'O':
				self.canvas.itemconfig(self.cubie_ids[i], fill='orange')
			elif self.cubie_color[i] == 'G':
				self.canvas.itemconfig(self.cubie_ids[i], fill='chartreuse2')
			elif self.cubie_color[i] == 'W':
				self.canvas.itemconfig(self.cubie_ids[i], fill='snow')
if __name__=="__main__":
	root = tk.Tk()
	cubie= Cubie(root)
	root.mainloop()