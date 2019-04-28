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
global canvas_update_speed

time = 0
loop_state = 'off'
canvas_update_speed = 100

''' SNAKE CLASS: Models a Snake on a 2D Grid Boardstate '''

class Snake:
    ''' Initialize Instance Attributes '''
    def __init__(self, name, body, color): 
        self.name = name
        self.body = body
        self.color = color
        self.grid_x = int(grid_size_x.get())
        self.grid_y = int(grid_size_y.get())
        self.energy = 300
        self.age = 0
        self.food_eaten = 0
        self.state = 'alive'
        
    def die(self):
        for elem in self.body:
            draw_plant(elem[0],elem[1])

        canvas.delete(self.name)
        print(self.name + " has died.")
        self.state = 'dead'

    def draw(self):
        ''' should only need to draw the head at every step. '''
        ''' moving is another option '''
        ''' simplest is to delete and redraw everything ?? '''
        body_length_index = len(self.body)-1
        
        for index,elem in enumerate(self.body):
            if index == 0:
                draw_rect(elem[0],elem[1],self.color,[self.name,'snake','tail'])
            elif index == body_length_index:
                draw_rect(elem[0],elem[1],self.color,[self.name,'snake','head'])                
            else:
                draw_rect(elem[0],elem[1],self.color,[self.name,'snake'])

    ''' All this just to draw eyes on the head as it moves.'''
    # It's a goddamn eyesore lmao.
    def draw_eyes(self):
        global x_step
        global y_step
        eye_tag = self.name
        eye_fill = 'black'
        ''' if: snake doesn't move '''
##        if self.body[-1][0]-self.body[-2][0] == 0 and self.body[-1][1]-self.body[-2][1] == 0:
##            x1 = self.body[-1][0]*x_step + 0.22*x_step
##            y1 = self.body[-1][1]*y_step + 0.22*y_step
##            x2 = self.body[-1][0]*x_step + 0.38*x_step
##            y2 = self.body[-1][1]*y_step + 0.38*y_step
##            canvas.create_rectangle(x1,y1,x2,y2,fill='red',tag=eye_tag)
##            x1 = self.body[-1][0]*x_step + 0.62*x_step
##            y1 = self.body[-1][1]*y_step + 0.22*y_step
##            x2 = self.body[-1][0]*x_step + 0.78*x_step
##            y2 = self.body[-1][1]*y_step + 0.38*y_step
##            canvas.create_rectangle(x1,y1,x2,y2,fill='red',tag=eye_tag)
        ''' snake goes up'''
        if self.body[-1][0]-self.body[-2][0] == 0 and self.body[-1][1]-self.body[-2][1] == 1:
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
        ''' snake goes right '''
        if self.body[-1][0]-self.body[-2][0] == 1 and self.body[-1][1]-self.body[-2][1] == 0:
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
        ''' snake goes down'''
        if self.body[-1][0]-self.body[-2][0] == 0 and self.body[-1][1]-self.body[-2][1] == -1:
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
        ''' snake goes left '''
        if self.body[-1][0]-self.body[-2][0] == -1 and self.body[-1][1]-self.body[-2][1] == 0:
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            
    def eat(self):
        ''' Don't define unchanging variables inside looped behaviour... '''
        global x_step
        global y_step
        global time

        [head_x,head_y] = self.head_xy(x_step,y_step)

        item_near = canvas.find_closest(head_x,head_y)
        item_tags = canvas.gettags(item_near)

        if (item_near and 'plant' in item_tags):
            #print(item_tags)
            item_x = canvas.coords(item_near)[0] + 0.5*x_step
            item_y = canvas.coords(item_near)[1] + 0.5*y_step
            if (abs(head_x - item_x) < x_step-1) and (abs(head_y - item_y) < y_step-1): 
                canvas.delete(item_near)
                self.energy += 5
                self.food_eaten += 1
                ''' every 30 food eaten snake grows '''
                if self.food_eaten % 30 == 0:
                    self.grow()
                    
    def grow(self):
        ''' Adds an extra segment to snake's body '''
        ''' Gen 01: Trigger in update_body(): after 50 pieces of food are eaten '''
        self.body = np.append(self.body,[self.body[-1]],axis=0)

        
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

        if self.age % 50 == 0:
            print(self.name + " has " + str(self.energy) + " energy.")
            
        canvas.delete(self.name) #only need to delete the tail and draw the head
        canvas.delete('eye')
        
        body_clipped = np.delete(self.body,0,0)
            
        ''' Genetic Algorithm '''
        ''' Gen 01: The snake randomly selects one of the four cardinal
            directions or chooses no movement and heads that way. '''

        rand_int = random.randint(1,100)
    
        if rand_int < 20:
            c = np.mod(body_clipped[-1]+[1,0],[self.grid_x,self.grid_y])
            self.energy += -1
        if (20 <= rand_int < 40):
            c = np.mod(body_clipped[-1]-[0,1],[self.grid_x,self.grid_y])
            self.energy += -1
        if (40 <= rand_int < 60):
            c = np.mod(body_clipped[-1]-[1,0],[self.grid_x,self.grid_y])
            self.energy += -1
        if (60 <= rand_int <= 80):
            c = np.mod(body_clipped[-1]+[0,1],[self.grid_x,self.grid_y])
            self.energy += -1
        if (80 <= rand_int <= 100):
            c = body_clipped[-1]
        
        ''' There's this whole stupid delete the entire body everytime
            thing too... Better is MOVE each body element? The head into
            a new square. The body and tail follows the segment immediately
            in front of it... todo '''
        
        body_clipper = np.append(body_clipped,[c],0)

        #print(body_clipper)
        self.body = body_clipper # nailed it! took long enough.

        self.eat() #eat before draw or snake eats own head.
        self.draw()
        self.draw_eyes()

        ''' view(): function test '''

        if (self.age % 500 == 0):
            global x_step
            global y_step
            self.view(x_step,y_step)
            #print(self.head_xy(x_step,y_step))
            #pause_loop()

        if (time % 100 == 0):
            print(self.name + " has " + str(self.energy) + " energy")

        if self.energy < 0:
            self.die()

        
    def view(self,x_step,y_step):
        ''' creates a matrix of surrounding area (snakes visual field) '''
        ''' gen 01: creates a 5x5 matrix: 0 for empty, 1 for plant, '''
        ''' 2 for own body, 3 for other snake. '''
        view_space = np.zeros([5,5])
        head_xy = self.head_xy(x_step,y_step)
        #print(view_space)
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        for n in range(0,5):
            for m in range(0,5):
                x1 = np.mod(head_xy[0] - 2*x_step + n*x_step - 1, width )
                x2 = np.mod(head_xy[0] - 2*x_step + n*x_step + 1, width )
                y1 = np.mod(head_xy[1] - 2*y_step + m*y_step - 1, height)
                y2 = np.mod(head_xy[1] - 2*y_step + m*y_step + 1, height) 
                #print(view_space[n,m])
                #canvas.create_rectangle([x1,y1],[(x2,y2],fill='red',tag='view')
                viewed_items = canvas.find_overlapping(x1, y1, x2, y2)
                for item in viewed_items:
                    item_tags = canvas.gettags(item)
                    # needs figuring...
                    ''' last item in the stack will take precedent '''
                    if 'plant' in item_tags:
                        view_space[n,m] = 1
                    if 'snake' in item_tags and self.name not in item_tags:
                        view_space[n,m] = 3
                        break
                    if self.name in item_tags:
                        view_space[n,m] = 2
                        break
                    
        #print(self.body[-1])
        view_space = np.transpose(view_space)
        print(view_space)
### END of Snake Class ###

''' General Purpose Functions '''
    
def initial_food_generation(p,row,col): 
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

def food_grow():
    ''' every 10 frames add three foods... '''
    n = int(grid_size_x.get())
    m = int(grid_size_y.get())
    a = random.randint(0,n)
    b = random.randint(0,m)
    draw_plant(a,b)

def generate_board():

    global x_step
    global y_step

    canvas.update()

    nrows = int(grid_size_x.get())
    ncols = int(grid_size_y.get())

    [x_step,y_step] = grid_steps()
    
    ''' necessary to resize snakes to new grid '''
    snake.grid_x = nrows
    snake.grid_y = ncols
    #print(snake.grid_x)
    snake2.grid_x = nrows
    snake2.grid_y = ncols
    
    
    canvas.delete('plant')
    p = int(Initial_Food_Entry.get())


    ''' delete and redraw snakes to match new grid size '''
    slith = [snake,snake2]
    for s in slith:
        canvas.delete(s.name)
        s.draw()
    
    #DrawGrid(nrows,ncols)
    initial_food_generation(p,nrows,ncols)

def grid_xy(n,m):
    ''' Returns x and y (Cartesian) canvas coordinates '''
    ''' Given grid-size (n x m) '''
    canvas.update()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    return [(canvas_width)/(n),(canvas_height)/(m)] # this isn't right...

def grid_steps():
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
    global canvas_update_speed

    if loop_state == 'on':
        time = time + 1
        time_string = "Time = " + str(time) 
        v.set(time_string)

        if snake.state == 'alive':
            snake.update_body()
        if snake2.state == 'alive':
            snake2.update_body()
        if snake.state == 'dead' and snake2.state == 'dead':
            pause_loop()

        '''add plant elements randomly'''
        #ensures the board state does not run out of food for snakes to eat.
        if time % 12 in [0,4,8]:
            food_grow()
        
        canvas.after(canvas_update_speed,canvas_update)

''' Frame Functions '''
# Button Toggles

def toggle_play():
    global loop_state
    global canvas_update_speed
    
    if loop_state == 'on':
        loop_state = 'off' #clicking play twice pauses the loop
        #print(Play_Button)
        canvas_update_speed = 100
        Play_Button.config(relief="raised")
    else:
        loop_state = 'on'
        Play_Button.config(relief="sunken")
        canvas_update()

def slow_loop():
    global canvas_update_speed
    canvas_update_speed = int(2*canvas_update_speed)

def fast_forward():
    global canvas_update_speed
    canvas_update_speed = int(0.5*canvas_update_speed)
        

def pause_loop():
    global loop_state
    global canvas_update_speed
    
    if loop_state == 'on':
        loop_state = 'off'
        Play_Button.config(relief="raised")
        canvas_update_speed = 100

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



''' Frames - Mostly for Sidebar GUI '''

# A A1
# B  X
#    Y
#    Z

frameA = Frame(root)
frameA.pack(expand=True,fill=BOTH)

frameA1 = Frame(frameA)
frameA1.pack(side='right')

frameX = Frame(frameA1)
frameX.pack(side='bottom')

frameY = Frame(frameA1)
frameY.pack(side='bottom')

frameZ = Frame(frameA1)
frameZ.pack(side='bottom')

frameZ1 = Frame(frameA1)
frameZ1.pack()

frameZ2 = Frame(frameA1)
frameZ1.pack(side='bottom')

''' Initialize Canvas '''
canvas = Canvas(frameA,width=300,height=300,bg="white",bd=1,relief="solid")
canvas.pack(expand=True,fill=BOTH,side='left')

frameB = Frame(root,bg='grey',bd=1)
frameB.pack()

''' Snake Label Below Canvas? '''
Snake_Label = Label(frameB,text="Test")
Snake_Label.pack()

''' Draw Grid - Entry Fields & Labels '''
Grid_Num_Rows = Label(frameA1,text="Grid Size = ")
Grid_Num_Rows.pack(side='left')

grid_size_x = Entry(frameA1,width=3)
grid_size_x.insert(10,'20')
grid_size_x.pack(side='left')

Grid_Label_x = Label(frameA1,text="×").pack(side='left')

grid_size_y = Entry(frameA1,width=3)
grid_size_y.insert(0,'20')
grid_size_y.pack(side='left')

''' Draw Grid Button '''
# Note: Buttons pack()ed inline are not recognised as Button objects.

##ToggleGrid_Button = Button(frame_gridbutton, width=12, text="Toggle Grid", command=DrawGrid)
##ToggleGrid_Button.pack(side='bottom')

''' Food Growth - Label & Entry '''
Food_Growth = Label(frameZ, text="Food Growth = ")
Food_Growth.pack(side='left')

Food_Growth_Entry = Entry(frameZ,width=2)
Food_Growth_Entry.insert(0,'10')
Food_Growth_Entry.pack(side='left')

''' Food Generation - Label & Entry '''
Initial_Food = Label(frameY, text="Initial Food = ")
Initial_Food.pack(side='left')

Initial_Food_Entry = Entry(frameY,width=2)
Initial_Food_Entry.insert(0,'33')
Initial_Food_Entry.pack(side='left')

Food_Label_2 = Label(frameY,text="%").pack(side='left')

''' Time Step Counter and Label '''
v = StringVar()
Time_Step_Label = Label(frameZ1, textvariable=v).pack()
time_string = "Time = " + str(time) 
v.set(time_string)

''' Boardstate Generation Button '''
Board_Set_Button = Button(frameZ1,text="Generate Board",command=generate_board) 
Board_Set_Button.pack()

''' Number of Snakes - Label and Entry Field '''

##Num_Snake_Label = Label(frame9,text="Number of Snakes: ").pack(side='left')
##Num_Snakes_Entry = Entry(frame9,width=2).pack(side='left')

##''' Slow Button '''
##slow_image = PhotoImage(file = 'slow_button.png')
##Slow_Button = Button(frame10,image=slow_image,command=slow_loop,relief="raised")
##Slow_Button.pack(side='left')

''' Play Button '''
play_image = PhotoImage(file = 'play_button.png')
Play_Button = Button(frameX,image=play_image,command=toggle_play,relief="raised")
Play_Button.pack(side='left')

''' Fast Forward Button '''
# Maybe better in terms of game enjoyability to have NO FF ??
fast_forward_img = PhotoImage(file = 'fast_forward_button.png')
Fast_Forward_Button = Button(frameX,image=fast_forward_img,command=fast_forward,relief="raised")
Fast_Forward_Button.pack(side='left')

''' Pause Button '''
pause_image = PhotoImage(file = 'pause_button.png')
Pause_Button = Button(frameX,image=pause_image,command=pause_loop)
Pause_Button.pack(side='left')


### Main ###
''' MAIN '''

canvas.update()
[x_step,y_step] = grid_steps() 

p = 33 # Initial proportion of food on canvas
m = 20 # Initial number of rows
n = 20 # Initial number of columns
initial_food_generation(p,m,n)

''' Initialize and Draw Snakes '''

body = np.array([[4,6],[5,6],[6,6]])
snake = Snake('jeffy',body,'#33CEFF')
snake.draw()

body2 = np.array([[7,10],[8,10],[9,10]])
snake2 = Snake('snakerella',body2,'#B953FF')
snake2.draw()

canvas.update()

#canvas.after(200, canvas_update)

root.mainloop()
