''' Genetic Program and Algorithm Test Design '''
''' 2D Implementation and GUI '''
### Working Title: Snakes on a (Cartesian) Plane ###

from tkinter import *
import numpy as np
import random

''' Global Variables and Initializations '''

global time
global loop_state
global x_step
global y_step

time = 0
loop_state = 'off'

''' SNAKE CLASS: Models a Snake on a 2D Grid Boardstate '''

class Snake:
    # Initializer / Instance Attributes
    def __init__(self, name, body, moves): 
        self.name = name
        self.body = body
        self.moves = moves # as yet unused
        self.grid_x = int(grid_size_x.get())
        self.grid_y = int(grid_size_y.get())
        self.energy = 0
        self.age = 0
        
    def draw(self):
        ''' should only need to draw the head at every step. '''
        ''' moving is another option '''
        ''' simplest is to delete and redraw everything ?? '''
        for elem in self.body:
            draw_rect(elem[0],elem[1],'grey',self.name)

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
        item_tags = canvas.gettags(item_yolo)

        if (item_yolo and 'plant' in item_tags):
            #print(item_tags)
            item_x = canvas.coords(item_yolo)[0]
            item_y = canvas.coords(item_yolo)[1]
            if (abs(head_x - item_x) < rect_x-1) and (abs(head_y - item_y) < rect_y-1): 
                if self.name not in item_tags:
                    canvas.delete(item_yolo)
                self.energy += 1
                if (self.energy % 50 == 0):
                    print(self.name + " has eaten " + str(self.energy) + " plants.")

    def head_xy(self,x_step,y_step):
        ''' Returns the xy (canvas) coordinates of the snake head... '''
        ''' cf: update_body() ''' # top-left corner
        head_x = self.body[-1][0]*x_step + 0.5*x_step
        head_y = self.body[-1][1]*y_step + 0.5*y_step
        return [head_x, head_y]
        
        
    def update_body(self):
        self.age += 1
        if (self.age % 1000 == 0):
            print(self.name + " is " + str(self.age) + " moves old.")
            
        canvas.delete(self.name) # delete snake body on canvas

        #body_clipped = np.delete(self.body,0,0)

        ''' Genetic Algorithm '''
        ''' Gen 01: The snake randomly selects one of the four cardinal
            directions or chooses no movement and heads that way. '''

        rand_int = random.randint(1,100) # generate random int in (1-100)
    
##        if rand_int < 20:
##            c = np.mod(body_clipped[-1],[self.grid_x,self.grid_y])
##        if (20 <= rand_int < 40):
##            c = np.mod(body_clipped[-1],[self.grid_x,self.grid_y])
##        if (40 <= rand_int < 60):
##            c = np.mod(body_clipped[-1],[self.grid_x,self.grid_y])
##        if (60 <= rand_int <= 80):
##            c = np.mod(body_clipped[-1],[self.grid_x,self.grid_y])
##        if (80 <= rand_int <= 100):
##            c = body_clipped[-1]
        
        ''' There's this whole stupid delete the entire body everytime
            thing too... Better is MOVE each body element? The head into
            a new square. The body and tail follows the segment immediately
            in front of it... todo '''
        
        #body_clipper = np.append(body_clipped,[c],0)

        #print(body_clipper)
        #self.body = body_clipper # nailed it! took long enough.

        self.eat()
        self.draw()

        if (self.age % 500 == 0):
            global x_step
            global y_step
            self.view(x_step,y_step)
            #print(self.head_xy(x_step,y_step))

    def view(self,x_step,y_step):
        ''' creates a matrix of surrounding area (snakes visual field) '''
        ''' gen 01: creates a 5x5 matrix: 0 for empty 1 for plant. '''
        view_space = np.zeros([5,5])
        head_xy = self.head_xy(x_step,y_step)
        #print(view_space)
        width = canvas.winfo_width()
        height = canvas.winfo_width()
        for n in range(0,5):
            for m in range(0,5):
                x1 = np.mod(head_xy[0] - 2*x_step + n*x_step - 2, width)
                x2 = np.mod(head_xy[0] - 2*x_step + n*x_step + 2, width)
                y1 = np.mod(head_xy[1] - 2*y_step + m*y_step - 2, height)
                y2 = np.mod(head_xy[1] - 2*y_step + m*y_step + 2, height) 
                #print(view_space[n,m])
                viewed_items = canvas.find_overlapping(x1, y1, x2, y2)
                for item in viewed_items:
                    item_tags = canvas.gettags(item)
                #canvas.create_rectangle([x1,y1],[x2,y2],fill='red',tag='view')
                #print(item_tags)
                    if 'plant' in item_tags:
                        view_space[n,m] = 1
                    if self.name in item_tags:
                        view_space[n,m] = 2
        #print(self.body[-1])
        view_space = np.transpose(view_space)
        print(view_space)
### END of Snake Class ###

''' General Purpose Functions '''
    
def Food_Generation(p,row,col): 
    for n in range(0,row):
        for m in range(0,col):
            if random.randint(0,100) < p:
                draw_plant(n,m)

def draw_plant(m,n):
    draw_rect(m,n,'green','plant')
    
def draw_rect(m,n,colour='grey',tagg='rect'):

    ''' Get grid size (n x m) from the grid_size x&y Entry fields '''
    grid_x = int(grid_size_x.get())
    grid_y = int(grid_size_y.get()) 

    ''' Necesarry to check definitions as grid entry fields may be empty. '''
    if (grid_x and grid_y):
        [rect_x,rect_y] = grid_xy(grid_x,grid_y)
        canvas.create_rectangle([(m)*(rect_x),(n)*(rect_y)],[(m+1)*(rect_x),(n+1)*(rect_y)],fill=colour,tag=tagg)

def generate_board():
    canvas.delete('plant')
    p = int(Initial_Food_Entry.get())

    nrows = int(grid_size_x.get())
    ncols = int(grid_size_y.get())

    snake1.grid_x = nrows
    snake1.grid_y = ncols
    #print(snake.grid_x)
    snake2.grid_x = nrows
    snake2.grid_y = ncols


    ''' delete and redraw snakes to match new grid size '''
    slith = [snake1,snake2]
    for s in slith:
        canvas.delete(s.name)
        s.draw()
    
    #DrawGrid(nrows,ncols)
    Food_Generation(p,nrows,ncols)

def grid_xy(n,m):
    ''' Returns x and y (Cartesian) canvas coordinates '''
    ''' Given grid-size (n x m) '''
    canvas.update()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    return [(canvas_width)/(n),(canvas_height)/(m)] # this isn't right...

def grid_step_xy():
    canvas.update()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    n = int(grid_size_x.get())
    m = int(grid_size_y.get())
    return [(canvas_width)/(n),(canvas_height)/(m)]
    

def canvas_update():
    """ update time counter """
    global time
    global loop_state

    if loop_state == 'on':
        time = time + 1
        time_string = "Time = " + str(time) 
        v.set(time_string)

        snake1.update_body()
        snake2.update_body()

        '''add plant elements randomly'''
        #ensures the board state does not run out of food for snakes to eat.
        
        canvas.after(100,canvas_update)

''' Frame Functions '''
# Button Toggles

def toggle_play():
    global loop_state
    
    if loop_state == 'on':
        loop_state = 'off' #clicking play twice pauses the loop
        #print(Play_Button) 
        Play_Button.config(relief="raised")
    else:
        loop_state = 'on'
        Play_Button.config(relief="sunken")
        canvas_update()
        

def pause_loop():
    global loop_state
    if loop_state == 'on':
        loop_state = 'off'
        Play_Button.config(relief="raised")

''' Initialize Root Window '''
root = Tk()
root.title("Snake 1.0")
root.config(padx=5,pady=5)

''' Get user's current screen resolution '''
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

padded_w = screen_width - 400   # Pad's user screen resolution.
padded_h = screen_height - 200  # Aesthetic for initial launch of program.

str_geometry = "%dx%d" % (padded_w,padded_h)

root.geometry(str_geometry)

''' Initialize Canvas '''
canvas = Canvas(width=300,height=300,bg="white",bd=1,relief="solid")
canvas.pack(expand=True,fill=BOTH,side='left')

''' Frames - Mostly for Sidebar GUI '''
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

''' Draw Grid - Entry Fields & Labels '''
Grid_Num_Rows = Label(frame2,text="Grid Size = ")
Grid_Num_Rows.pack(side='left')

grid_size_x = Entry(frame2,width=3)
grid_size_x.insert(10,'20')
grid_size_x.pack(side='left')

Grid_Label_x = Label(frame2,text="×").pack(side='left')

grid_size_y = Entry(frame2,width=3)
grid_size_y.insert(0,'20')
grid_size_y.pack(side='left')

''' Draw Grid Button '''
# Note: Buttons pack()ed inline are not recognised as Button objects.

##ToggleGrid_Button = Button(frame_gridbutton, width=12, text="Toggle Grid", command=DrawGrid)
##ToggleGrid_Button.pack(side='bottom')

''' Food Generation - Label & Entry '''
Initial_Food = Label(frame7, text="Initial Food = ")
Initial_Food.pack(side='left')

Initial_Food_Entry = Entry(frame7,width=2)
Initial_Food_Entry.insert(0,'33')
Initial_Food_Entry.pack(side='left')

Food_Label_2 = Label(frame7,text="%").pack(side='left')

''' Time Step Counter and Label '''
v = StringVar()
Time_Step_Label = Label(frame8, textvariable=v).pack()
time_string = "Time = " + str(time) 
v.set(time_string)


''' Boardstate Generation Button '''
Board_Set_Button = Button(frame_board,text="Generate Board",command=generate_board) 
Board_Set_Button.pack()

''' Number of Snakes - Label and Entry Field '''

##Num_Snake_Label = Label(frame9,text="Number of Snakes: ").pack(side='left')
##Num_Snakes_Entry = Entry(frame9,width=2).pack(side='left')

''' Play Button '''
play_image = PhotoImage(file = 'play_button.png')
Play_Button = Button(frame10,image=play_image,command=toggle_play,relief="raised")
Play_Button.pack(side='left')

''' Fast Forward Button '''
fast_forward_img = PhotoImage(file = 'fast_forward_button.png')
Fast_Forward_Button = Button(frame10,image=fast_forward_img,command=canvas_update,relief="raised")
Fast_Forward_Button.pack(side='left')

''' Pause Button '''
pause_image = PhotoImage(file = 'pause_button.png')
Pause_Button = Button(frame10,image=pause_image,command=pause_loop)
Pause_Button.pack(side='left')


### Main ###
''' MAIN '''

canvas.update()
[x_step,y_step] = grid_step_xy() 

p = 33 # Proportion of food on boardspace
Food_Generation(p,20,20)

''' Initialize and Draw Snakes '''

body = np.array([[6,6],[6,7],[6,8],[7,8]])
snake1 = Snake('jeffy',body,1)
snake1.draw()

body2 = np.array([[11,11],[11,12],[11,13],[12,13]])
snake2 = Snake('snakerella',body2,1)
snake2.draw()

canvas.update()

#canvas.after(200, canvas_update)

root.mainloop()
