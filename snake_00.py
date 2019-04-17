# Genetic Program Test: Snake 2D

from tkinter import *
import numpy as np
import math
import random

# Functions

class Snake:
    # Initializer / Instance Attributes
    def __init__(self, name, body, moves, grid_x, grid_y):
        self.name = name
        self.body = body
        self.moves = moves
        self.grid_x = grid_x
        self.grid_y = grid_y
        
    def draw(self):
        for elem in self.body:
            DrawRect(elem[0],elem[1],'grey',self.name)

    def update_body(self):
        canvas.delete(self.name)

        body_clipped = np.delete(self.body,0,0)

        rand_int = random.randint(1,100)
    
        if rand_int < 25:
            c = np.mod(body_clipped[-1]+[1,0],[self.grid_x,self.grid_y])
        if (25 <= rand_int < 50):
            c = np.mod(body_clipped[-1]-[0,1],[self.grid_x,self.grid_y])
        if (50 <= rand_int < 75):
            c = np.mod(body_clipped[-1]-[1,0],[self.grid_x,self.grid_y])
        if (75 <= rand_int <= 100):
            c = np.mod(body_clipped[-1]+[0,1],[self.grid_x,self.grid_y])

        body_clipper = np.append(body_clipped,[c],0)

        #print(body_clipper)
        self.body = body_clipper # nailed it!

    def eat(self):
        '''obviously we don't want to define unchanging variables inside LOOPED behaviour but c'est la vie'''
        grid_x = int(grid_size_x.get())
        grid_y = int(grid_size_y.get())

        canvas.update()
        
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        rect_x = (canvas_width)/(grid_x)
        rect_y = (canvas_height)/(grid_y)
    
        #print(self.body[-1][0])
        #print(self.body[-1][0]*rect_x)
        #print(self.body[-1][1]*rect_y)

        head_x = self.body[-1][0]*rect_x
        head_y = self.body[-1][1]*rect_y

        item_yolo = canvas.find_closest(head_x,head_y)
        item_x = canvas.coords(item_yolo)[0]
        item_y = canvas.coords(item_yolo)[1]
        if (abs(head_x - item_x) < rect_x) and (abs(head_y - item_y) < rect_y): 
            canvas.delete(item_yolo)
            
def Food_Generation(p,row,col): 
    for n in range(1,row+1):
        for m in range(1,col+1):
            if random.randint(0,100) < p:
                draw_plant(n,m)

def draw_plant(row,column):
    DrawRect(row,column,'green','plant')
    
def DrawRect(m,n,colour='grey',tagg = 'rect'):
    
    grid_x = int(grid_size_x.get())
    grid_y = int(grid_size_y.get())

    canvas.update()
    
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    rect_x = (canvas_width)/(grid_x)
    rect_y = (canvas_height)/(grid_y)
    
    canvas.create_rectangle([(m)*(rect_x),(n)*(rect_y)],[(m+1)*(rect_x),(n+1)*(rect_y)],fill=colour,tag=tagg)

def DrawRect_From_Entry(m=2,n=2,colour='grey'):
    grid_x = int(grid_size_x.get())
    grid_y = int(grid_size_y.get())

    canvas.update()

    n = int(Rect_Row_Entry.get())
    m = int(Rect_Col_Entry.get())
    
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    rect_x = (canvas_width)/(grid_x)
    rect_y = (canvas_height)/(grid_y)
    
    canvas.create_rectangle([(m-1)*(rect_x),(n-1)*(rect_y)],[m*(rect_x),n*(rect_y)],fill=colour,tag='rect')

def generate_board():
    canvas.delete('plant')
    p = int(Initial_Food_Entry.get())
    nrows = int(grid_size_x.get())
    ncols = int(grid_size_y.get())
    snake.grid_x = nrows
    #print(snake.grid_x)
    snake.grid_y = ncols
    #DrawGrid(nrows,ncols)
    Food_Generation(p,nrows,ncols)

def canvas_update():
    """ update time counter """
    global time
    global loop_state

    if loop_state == 'on':
        time = time + 1
        time_string = "Time = " + str(time) 
        v.set(time_string)

        snake.update_body()
        snake.eat()
        snake.draw()

        snake2.update_body()
        snake2.eat()
        snake2.draw()
    
        canvas.after(100,canvas_update)

def toggle_play():
    global loop_state
    
    if loop_state == 'on':
        loop_state = 'off' # pause_loop()
    if loop_state == 'off':
        loop_state = 'on'
        canvas_update()
        

def pause_loop():
    global loop_state
    loop_state = 'off'
    
# Initialize Variables 

global time
global loop_state

time = 0
loop_state = 'off'

# Initialize Root Window

root = Tk()
root.title("Snake 1.0")
root.config(padx=5,pady=5)

# Get user's current screen resolution.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

padded_w = screen_width - 400   # Pad's user screen resolution.
padded_h = screen_height - 200

str_geometry = "%dx%d" % (padded_w,padded_h)

root.geometry(str_geometry)

# Initialize Canvas

canvas = Canvas(width=300,height=300,bg="white",bd=1,relief="solid")
canvas.pack(expand=True,fill=BOTH,side='left')

# Frames - Holy bad practices, Batman!

frame = Frame(root)
frame.pack(side='top')

frame2 = Frame(frame)
frame2.pack()

frame3 = Frame(frame)
frame3.pack()

frame_gridbutton = Frame(frame)
frame_gridbutton.pack()

frame4 = Frame(frame)
frame4.pack()

frame5 = Frame(frame)
frame5.pack()

frame6 = Frame(frame)
frame6.pack()

frame7 = Frame(frame)
frame7.pack()

frame8 = Frame(frame)
frame8.pack()

frame9 = Frame(frame)
frame9.pack()

frame_board = Frame(frame)
frame_board.pack()

frame10 = Frame(frame)
frame10.pack()

# Draw Grid - Entry Fields & Labels

Grid_Num_Rows = Label(frame2,text="Grid Size = ")
Grid_Num_Rows.pack(side='left')

grid_size_x = Entry(frame2,width=3)
grid_size_x.insert(10,'20')
grid_size_x.pack(side='left')

Grid_Label_x = Label(frame2,text="×").pack(side='left')

grid_size_y = Entry(frame2,width=3)
grid_size_y.insert(0,'20')
grid_size_y.pack(side='left')

# Draw Grid - Button

##ToggleGrid_Button = Button(frame_gridbutton, width=12, text="Toggle Grid", command=DrawGrid)
##ToggleGrid_Button.pack(side='bottom')

# Food Generation - Label & Entry

Initial_Food = Label(frame7, text="Initial Food = ")
Initial_Food.pack(side='left')

Initial_Food_Entry = Entry(frame7,width=2)
Initial_Food_Entry.insert(0,'33')
Initial_Food_Entry.pack(side='left')

Food_Label_2 = Label(frame7,text="%").pack(side='left')

# Time Step - Label

v = StringVar()
Time_Step_Label = Label(frame8, textvariable=v).pack()
time_string = "Time = " + str(time) 
v.set(time_string)


# Reset Board - Button

Board_Set_Button = Button(frame_board,text="Generate Board",command=generate_board) 
Board_Set_Button.pack()

# Number of Snakes - Label and Entry Field

Num_Snake_Label = Label(frame9,text="Number of Snakes: ").pack(side='left')
Num_Snakes_Entry = Entry(frame9,width=2).pack(side='left')

# Play Button

play_image = PhotoImage(file = 'play_button.png')
Play_Button = Button(frame10,image=play_image,command=toggle_play).pack(side='left')

# Pause Button

pause_image = PhotoImage(file = 'pause_button.png')
Pause_Button = Button(frame10,image=pause_image,command=pause_loop).pack(side='left')


### Main ###

# DrawGrid(20,20)

grid_x = int(grid_size_x.get())
grid_y = int(grid_size_y.get())

body = np.array([[1,1],[1,2],[1,3],[2,3],[2,4],[3,4],[3,5],[3,6],[4,6],[5,6],[6,6]])
snake = Snake('jeff',body,1,grid_x,grid_y)
snake.draw()

body2 = np.array([[5,5],[5,6],[5,7],[6,7],[6,8],[7,8],[7,9],[7,10],[8,10],[9,10],[10,10]])
snake2 = Snake('jeffu',body2,1,grid_x,grid_y)
snake2.draw()

p = 33
#Food_Generation(p,20,20)

canvas.update()

#canvas.after(200, canvas_update)

root.mainloop()
